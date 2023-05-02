# SnowChatSQL

A Streamlit app that allows users to analyze data in a Snowflake data warehouse using natural language. 

## Overview
This app is a POC on the ability to analyze any dataset that is stored in a Snowflake database using AI and natural language. 
I used a free sample dataset from the Snowflake Marketplace on ***Amazon Vendor Analytics***.


### Snowflake Sample Dataset: ***Amazon Vendor Analytics***
https://app.snowflake.com/marketplace/listing/GZTYZ3HT1R1/reason-automation-amazon-vendor-analytics-sample-dataset

## Tech Stack
- [Streamlit](https://streamlit.io/) - Python Data App framework
- [Snowflake](https://www.snowflake.com/) - Data Warehouse
- [ChromaDB](https://www.trychroma.com/) - Vector Store
- [OpenAI](https://openai.com/) (text-davinci-003) - Large Language Model (LLM)

## Install Dependencies
- `poetry env use 3.8.16` - Make sure poetry uses the correct Python version.
- `poetry install` - This will install all the dependencies in the `pyproject.toml` file.

Note: This project uses Poetry for local development. However Streamlit requires a `requirements.txt` file for deployment. 
Use the following command to generate the `requirements.txt` file from Poetry.

`poetry export --without-hashes --format=requirements.txt > requirements.txt`

## Configure Python Interpreter in VSCode:
- `CMD + SHIFT + P` -> `Python: Select Interpreter` -> Select the `Python 3.8.16 ('.venv': poetry)` option.

## Run:
- `streamlit run src/Home.py`
- From VS Code, see the `launch.json` file.

## Env variables:
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
