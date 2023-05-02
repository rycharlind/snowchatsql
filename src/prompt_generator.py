# create a class will that will be used to generate the prompt from the chromadb schema

from snowchatsql.config.config import Config
from snowchatsql.prompt_builder import PromptBuilder
from snowchatsql.vector_store import VectorStore
import openai
import util.io_base as io_base


class PromptGenerator():
    def __init__(self, config: Config):
        self.config = config
        self.vector_store = VectorStore(config)
        self.prompt_builder = PromptBuilder()

    def get_prompt_template(self, prompt_schema: str):
        return f"""Snowflake SQL tables, with their properties:
{prompt_schema}
You are a business owner who sells products on Amazon.com that needs to understand the data in Snowflake.
Generate 5 questions that you would ask about the above Snowflake tables in aggregate.
Do not number your questions. Separate them with a blank line.
Do not reference exact table names or fields names in your response.
You are asking a business analyst questions who will query Snowflake to get results.
Your response should be able to be converted into a Snowflake SQL query if provided back to you."""

    def run(self):
        prompts = []
        docs = self.vector_store.get_all_docs(self.config.chroma.collection_name)
        for i in range(0, len(docs), 5):
            chunk = docs[i:i+5]
            chunk_prompt = self.prompt_builder.build_from_documents(chunk)
            prompt = self.get_prompt_template(chunk_prompt)
            prompts.append(prompt)
        
        self.write_prompts(prompts)

        for index, prompt in enumerate(prompts):
            try:
                response = self.get_ai_prompt_response(prompt).strip()
                print(response)
                io_base.write_text(response, f"./prompts/stg2/questions_{index}.txt")
            except Exception as e:
                print(e)

    def write_prompts(self, prompts: list):
        for index, prompt in enumerate(prompts):
            io_base.write_text(prompt, f"./prompts/stg1/prompt_{index}.txt")

    def get_ai_prompt_response(self, prompt: str) -> str:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=550,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        return response["choices"][0]["text"]

if __name__ == "__main__":
    config = Config()
    prompt_generator = PromptGenerator(config)
    prompt_generator.run()
