import os
from snowchatsql.c_env import CEnv


class ConfigChroma():
    def __init__(self):
        self.db_dir = os.getenv(CEnv.CHROMA_DB_DIR)