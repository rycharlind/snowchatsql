import os
from snowchatsql.c_env import CEnv


class ConfigSnowflake():
    def __init__(self):
        self.account = os.getenv(CEnv.SNOWFLAKE_ACCOUNT)
        self.user = os.getenv(CEnv.SNOWFLAKE_USER)
        self.password = os.getenv(CEnv.SNOWFLAKE_PASSWORD)
        self.warehouse = os.getenv(CEnv.SNOWFLAKE_WAREHOUSE)
        self.database = os.getenv(CEnv.SNOWFLAKE_DATABASE)
        self.schema = os.getenv(CEnv.SNOWFLAKE_SCHEMA)
