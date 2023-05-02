import streamlit as st
import openai
from snowchatsql.c_state import CState
from snowchatsql.snowflake import Snowflake
from snowchatsql.config.config import Config
from snowchatsql.vector_store import VectorStore
from snowchatsql.prompt_builder import PromptBuilder

st.set_page_config(layout='wide')
st.header("Chat SQL")

config = Config()
snowflake = Snowflake(config)
vector_store = VectorStore(config)
prompt_builder = PromptBuilder()

if CState.CHAT_GENERATED not in st.session_state:
    st.session_state[CState.CHAT_GENERATED] = []

if CState.CHAT_PAST not in st.session_state:
    st.session_state[CState.CHAT_PAST] = []

if CState.RESULT_DATAFRAME not in st.session_state:
    st.session_state[CState.RESULT_DATAFRAME] = []

st.caption("Use the below text area to enter your prompt. The prompt will be used to generate a SQL query. The query will be executed against Snowflake and the results will be displayed below.")

prompt = st.text_area("Enter your prompt here", key=CState.CHAT_PROMPT)


if prompt:
    related_documents = vector_store.search(prompt=prompt, collection_name=config.chroma.collection_name)
    prompt_schema = prompt_builder.build_from_documents(related_documents)
    prompt_final = prompt_builder.get_prompt_template(prompt_schema, prompt=prompt)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_final,
        temperature=0,
        max_tokens=250,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["#", ";"]
    )

    output = response["choices"][0]["text"]

    st.session_state[CState.CHAT_GENERATED].append(output)
    st.session_state[CState.CHAT_PAST].append(prompt)

    try:
        df = snowflake.sql(output)
        st.session_state[CState.RESULT_DATAFRAME].append(df)
    except Exception as e:
        st.warning("Could not execute this SQL. It may need some manual tweaking.")

if st.session_state[CState.CHAT_GENERATED]:

    for i in range(len(st.session_state[CState.CHAT_GENERATED]) - 1, -1, -1):
        st.info(st.session_state[CState.CHAT_PAST][i])
        st.code(st.session_state[CState.CHAT_GENERATED][i], language="sql")
        st.dataframe(st.session_state[CState.RESULT_DATAFRAME][i])
        st.divider()
