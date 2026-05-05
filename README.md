# 知识图谱可视化系统

一个基于Python的文档知识图谱生成和可视化系统。

## 功能特点

- 📁 支持多种文档格式：PDF、DOCX、PPTX、TXT
- 🧠 自动从文档中提取知识实体和关系
- 🌐 动态知识网络可视化
- 🔍 点击节点查看原文上下文
- 📊 支持多文档同时处理

## 项目结构

```
knowledge-graph/
├── app.py                  # Flask后端应用
├── knowledge_extractor.py  # 文档解析和知识提取模块
├── requirements.txt        # Python依赖
├── templates/
│   └── index.html         # 前端界面
└── uploads/               # 上传文件目录（自动创建）
```

## 安装步骤

1. 安装Python依赖：
```bash
pip install -r requirements.txt
```

## 运行程序

```bash
python app.py
```

然后在浏览器中访问：http://localhost:5000

## 使用说明

1. 点击或拖拽文档到上传区域
2. 选择一个或多个文档（PDF、DOCX、PPTX、TXT格式）
3. 点击"生成知识图谱"按钮
4. 等待分析完成，查看生成的知识图谱
5. 点击图谱中的节点，右侧会显示该关键词在原文中的相关内容

## 技术栈

- **后端**：Flask + Python
- **文档解析**：PyPDF2, python-docx, python-pptx
- **知识提取**：jieba（中文分词）
- **图算法**：NetworkX
- **可视化**：Vis.js
