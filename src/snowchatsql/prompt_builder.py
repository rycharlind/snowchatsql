class PromptBuilder():

    def get_prompt_template(self, prompt_schema: str, prompt: str):
        return f"""### Snowflake SQL tables, with their properties:
#
{prompt_schema}
#
###
{prompt}
"""

    def build_from_schema(self, schema):
        schema_str = ""
        for table, fields in schema.items():
            out = self.get_schema_prompt(table, fields)
            schema_str += f"{out}\n"

        return schema_str
    
    def build_from_documents(self, documents: list) -> str:
        out = "\n".join(list(map(lambda document: document, documents)))
        return f"{out}"
    
    def get_schema_prompt(self, table: str, fields: list) -> str:
        return f"{table} ({', '.join(list(map(lambda field: self.get_field_line(field), fields)))})))"
    
    def get_field_line(self, field) -> str:
        return f"{field['name']} ({field['type']})"
    
    def get_table_schema_str_list(self, tables: list) -> list:
        return list(map(lambda table: self.get_table_schema_prompt(table), tables))
    
    def get_table_schema_final_prompt(self, table_schema_str_list: list) -> str:
        out = "\n".join(list(map(lambda table_schema_str: table_schema_str, table_schema_str_list)))
        return f"{out}"
    
    

