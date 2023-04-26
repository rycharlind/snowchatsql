from snowchatsql.config.config import Config
from snowchatsql.snowflake import Snowflake
from snowchatsql.vector_store import VectorStore
from snowchatsql.prompt_builder import PromptBuilder

config = Config()
prompt_builder = PromptBuilder()
snowflake = Snowflake(config)
vector_store = VectorStore(config)

tables = snowflake.get_tables()
schema = {table: snowflake.get_table_fields(table) for table in tables}

table_fields = []
for table, fields in schema.items():
    table_fields.append(prompt_builder.get_schema_prompt(table, fields))

vector_store.persist_database_schema(config.chroma.collection_name, tables, table_fields)