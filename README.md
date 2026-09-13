# Agent — 扫地机器人智能客服系统

基于 **Streamlit + LangChain ReAct Agent + RAG（ChromaDB 向量库）** 构建的智能客服应用，知识库为扫地机器人领域的常见问题，支持流式输出对话。

## 项目简介

用户通过 Web 聊天界面提问（如故障排查、维护保养、选购建议等），系统基于本地知识库检索增强生成回答。核心是一个 LangChain ReAct Agent，具备多种工具调用能力（RAG 检索总结、天气查询、用户定位、外部数据获取、使用报告生成等），并通过中间件实现工具调用监控、日志记录与提示词切换。

## 技术栈

- Python + Streamlit（Web 界面）
- LangChain（ReAct Agent 编排）
- ChromaDB（向量数据库）
- 通义千问系列模型（对话模型 qwen3.7-max、Embedding 模型 text-embedding-v1）

## 目录结构

```
Agent/
├── app.py                  # Streamlit 入口，聊天界面
├── agent/
│   ├── react_agent.py      # ReAct Agent 核心实现（流式输出）
│   └── tools/
│       ├── agent_tools.py  # 工具定义（rag_summarize / get_weather / fetch_external_data 等）
│       └── middleware.py   # 中间件（工具监控、模型日志、报告提示词切换）
├── rag/
│   ├── rag_service.py      # RAG 检索服务
│   └── vector_store.py     # ChromaDB 向量库封装
├── model/
│   └── factory.py          # 对话模型工厂
├── config/
│   ├── agent.yml           # Agent 配置（外部数据路径）
│   ├── chroma.yml          # 向量库配置
│   ├── prompts.yml         # 提示词配置
│   └── rag.yml             # RAG 模型配置
├── prompts/
│   ├── main_prompt.txt     # 主提示词
│   ├── rag_summarize.txt   # RAG 总结提示词
│   └── report_prompt.txt   # 报告生成提示词
├── data/
│   ├── 扫地机器人100问.pdf / .txt    # 知识库原始资料
│   ├── 扫拖一体机器人100问.txt
│   ├── 故障排除.txt / 维护保养.txt / 选购指南.txt
│   └── external/records.csv          # 外部数据
├── utils/                  # 配置、文件、日志、提示词等工具函数
├── logs/                   # 运行日志
└── chroma_db/              # 向量库持久化目录
```

## 运行方式

```bash
# 安装依赖（streamlit / langchain / chromadb / dashscope 等）
pip install -r requirements.txt   # 如有

# 启动 Web 界面
streamlit run app.py
```

## 注意事项

- 模型调用依赖 DashScope（阿里云百炼）API Key，需在 `model/factory.py` 或环境变量中配置。
- 首次运行会自动将 `data/` 下的知识库文档向量化写入 `chroma_db/`。
