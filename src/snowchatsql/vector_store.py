import chromadb
from chromadb.config import Settings
from snowchatsql.config.config import Config
import os

class VectorStore():
    def __init__(self, config: Config) -> None:
        project_root = os.path.dirname(os.path.abspath(__file__))
        self.chroma_client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=os.path.join(project_root, "chroma_db_data") # todo: This is temp. Will eventually move to cloud storage.
        ))

    # Returns a list of documents that match the prompt.
    def search(self, collection_name: str, prompt: str, n_results: int = 5):
        collection = self.chroma_client.get_collection(name=collection_name)
        result = collection.query(
            query_texts=[prompt],
            n_results=n_results
        )
        documents = result['documents'][0]
        return documents
    
    def get_all_docs(self, collection_name: str):
        collection = self.chroma_client.get_collection(name=collection_name)
        return collection.get()['documents']

    # Saves a document for each table schema. 
    def persist_database_schema(self, database_name: str, tables: list, table_schemas: list) -> None:
        try:
            c = self.chroma_client.get_collection(name=database_name)
            if (c is not None):
                self.chroma_client.delete_collection(name=database_name)
                print(f"Deleted existing collection {database_name}")
        except:
            print("Collection does not exist. Proceeding to create it.")


        collection = self.chroma_client.create_collection(name=database_name)
        collection.add(
            documents=table_schemas,
            ids=tables
        )
        
        print(f"Persisted database schema for {database_name}")