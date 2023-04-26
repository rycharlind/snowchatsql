import chromadb
from chromadb.config import Settings
from snowchatsql.config.config import Config

class VectorStore():
    def __init__(self, config: Config) -> None:
        self.chroma_client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=config.chroma.db_dir
        ))

    def persist_database_schema(self, database: str, schema: str) -> None:
        collection = self.chroma_client.create_collection(name=f"{database}_schema")
        collection.add(
            documents=[schema],
            ids=[f"{database}_schema"]
        )
        print(f"Persisted database schema for {database}")