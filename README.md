# SnowChatSQL

## Install Dependencies
- `poetry env use 3.8.16` - Make sure poetry uses the correct Python version.
- `poetry install` - This will install all the dependencies in the `pyproject.toml` file.

## Configure Python Interpreter in VSCode:
- `CMD + SHIFT + P` -> `Python: Select Interpreter` -> Select the `Python 3.8.16 ('.venv': poetry)` option.

## Run:
- `streamlit run src/Home.py`
- From VS Code, see the `launch.json` file.

## Env variables for Snowflake connection:
```
SNOWFLAKE_ACCOUNT="<account_id>.central-us.azure"
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
