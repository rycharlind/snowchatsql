# SnowChatSQL

A Streamlit app that allows users to analyze data in a Snowflake data warehouse using natural language. 

## Stack
- Streamlit - Python Data App framework
- Snowflake - Data Warehouse
- ChromaDB - Vector Store
- OpenAI (GPT4) - Large Language Model (LLM)

## Install Dependencies
- `poetry env use 3.8.16` - Make sure poetry uses the correct Python version.
- `poetry install` - This will install all the dependencies in the `pyproject.toml` file.

## Configure Python Interpreter in VSCode:
- `CMD + SHIFT + P` -> `Python: Select Interpreter` -> Select the `Python 3.8.16 ('.venv': poetry)` option.

## Run:
- `streamlit run src/Home.py`
- From VS Code, see the `launch.json` file.

## Env variables for Snowflake connection:
```bash
# OpenAI
OPENAI_API_KEY=""

# ChromaDB
CHROMA_DB_DIR=""

# Snowflake
SNOWFLAKE_ACCOUNT="<account_id>.us-east-2.aws"
SNOWFLAKE_USER=""
SNOWFLAKE_PASSWORD=""
SNOWFLAKE_DATABASE=""
SNOWFLAKE_WAREHOUSE=""
SNOWFLAKE_SCHEMA=""
```

## Refs:
- https://docs.streamlit.io/
- https://docs.snowflake.com/en/developer-guide/snowpark/python/setup.html
- https://realpython.com/intro-to-pyenv
- https://python-poetry.org/
