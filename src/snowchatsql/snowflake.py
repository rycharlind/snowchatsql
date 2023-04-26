from snowflake.snowpark import Session
from snowchatsql.config.config import Config

class Snowflake():
    def __init__(self, config: Config) -> None:
        self.config = config
        self.session = self.get_session()

    def get_session(self) -> Session:
        connection_parameters = {
            "account": self.config.snowflake.account,
            "user": self.config.snowflake.user,
            "password": self.config.snowflake.password,
            "warehouse": self.config.snowflake.warehouse,
            "database": self.config.snowflake.database,
            "schema": self.config.snowflake.schema
        }
        
        return Session.builder.configs(connection_parameters).create()

    def get_tables(self) -> list:
        tables = self.session.sql(f"SHOW TABLES").collect()
        return list(map(lambda table: table.name, tables))
    
    def get_table_schema(self, table: str) -> list:
        schema = self.session.sql(f"DESCRIBE TABLE {table}").collect()
        return list(map(lambda column: {'name': column.name, 'type': column.type}, schema))