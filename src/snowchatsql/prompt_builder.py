class PromptBuilder():

    def get_prompt_template(self, prompt_schema: str, prompt: str):
        return f"""
### Snowflake SQL tables, with their properties:
#
{prompt_schema}
#
###
{prompt}
"""

    def build_from_table_schemas(self, schemas: list) -> str:
        out = "\n".join(list(map(lambda schema: schema, schemas)))
        return f"{out}"
    
    def get_schema_prompt(self, table: str, schema: list) -> str:
        return f"{table} ({', '.join(list(map(lambda column: self.get_schema_line(column), schema)))})))"
    
    def get_schema_line(self, column) -> str:
        return f"{column['name']} ({column['type']})"
    
    def get_table_schema_str_list(self, tables: list) -> list:
        return list(map(lambda table: self.get_table_schema_prompt(table), tables))
    
    def get_table_schema_final_prompt(self, table_schema_str_list: list) -> str:
        out = "\n".join(list(map(lambda table_schema_str: table_schema_str, table_schema_str_list)))
        return f"{out}"
    
    def get_prompt_schema_from_documents(self, documents: list) -> str:
        out = "\n".join(list(map(lambda document: document, documents)))
        return f"{out}"
    

