import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from knowledge_extractor import KnowledgeGraphGenerator

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'pptx', 'txt'}

graph_generator = None


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_files():
    global graph_generator

    if 'files' not in request.files:
        return jsonify({'error': 'No files uploaded'}), 400

    files = request.files.getlist('files')
    if not files or files[0].filename == '':
        return jsonify({'error': 'No files selected'}), 400

    file_paths = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            file_paths.append(file_path)

    if not file_paths:
        return jsonify({'error': 'No valid files uploaded'}), 400

    graph_generator = KnowledgeGraphGenerator()
    G = graph_generator.build_graph(file_paths)
    graph_data = graph_generator.graph_to_json(G)

    return jsonify({
        'success': True,
        'graph': graph_data,
        'file_count': len(file_paths)
    })


@app.route('/context', methods=['POST'])
def get_context():
    global graph_generator

    if not graph_generator:
        return jsonify({'error': 'No graph loaded'}), 400

    data = request.json
    entity = data.get('entity')

    if not entity:
        return jsonify({'error': 'No entity specified'}), 400

    contexts = graph_generator.get_entity_context(entity)
    return jsonify({'contexts': contexts})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
