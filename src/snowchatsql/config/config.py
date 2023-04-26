import os
from snowchatsql.config.config_aws import ConfigAws
from snowchatsql.config.config_snowflake import ConfigSnowflake
from snowchatsql.config.config_chroma import ConfigChroma
from snowchatsql.c_env import CEnv


class Config():
    def __init__(self):
        self.openai_api_key = os.getenv(CEnv.OPENAI_API_KEY)
        self.aws = ConfigAws()
        self.snowflake = ConfigSnowflake()
        self.chroma = ConfigChroma()