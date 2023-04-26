import streamlit as st
from snowchatsql.config.config import Config
from snowchatsql.c_state import CState
from snowchatsql.snowflake import Snowflake
from snowchatsql.vector_store import VectorStore
from snowchatsql.prompt_builder import PromptBuilder

st.set_page_config(layout='wide')
st.header("Prompt Settings")

config = Config()
prompt_builder = PromptBuilder()
snowflake = Snowflake(config)
vector_store = VectorStore(config)

prompt = st.text_area("Prompt Template", key=CState.CHAT_PROMPT_TEMPLATE)

generate = st.button("Generate Prompt Template")

if (generate):
    tables = snowflake.get_tables()
    schemas = list(map(lambda table: snowflake.get_table_schema(table), tables))
    st.write(schemas)
