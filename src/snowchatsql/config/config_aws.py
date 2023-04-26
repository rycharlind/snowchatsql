import os
from snowchatsql.c_env import CEnv


class ConfigAws():
    def __init__(self):
        self.aws_key = os.getenv(CEnv.AWS_ACCESS_KEY_ID)
        self.aws_secret = os.getenv(CEnv.AWS_SECRET_ACCESS_KEY)
        self.aws_s3_bucket = os.getenv(CEnv.AWS_S3_BUCKET)