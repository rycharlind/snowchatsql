class PromptBuilder():

    def get_prompt_template(self, prompt_schema: str, prompt: str):
        return f"""### Snowflake SQL tables, with their properties:
#
{prompt_schema}
#
{prompt}
#
Respond only in Snowflake SQL.
If you don't know what value to use for a field, do your best to fill it in so that the SQL will execute properly.
###
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

    
    

