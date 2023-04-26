import streamlit as st
import openai
import os
from core.snow_session import SnowSession
from core.state_key import StateKey

st.set_page_config(layout='wide')

openai.api_key = os.getenv("OPENAI_API_KEY")

snow_session = SnowSession.get_session()



if StateKey.CHAT_GENERATED not in st.session_state:
    st.session_state[StateKey.CHAT_GENERATED] = []

if StateKey.CHAT_PAST not in st.session_state:
    st.session_state[StateKey.CHAT_PAST] = []

if StateKey.RESULT_DATAFRAME not in st.session_state:
    st.session_state[StateKey.RESULT_DATAFRAME] = []

st.header("Chat SQL")

prompt = st.text_area("Enter your prompt here", key=StateKey.CHAT_PROMPT)


def get_prompt_template(prompt: str):
    return f"""
### Snowflake SQL tables, with their properties:
#
# ch_patient(patient_key, first_name, last_name, birth_date, gender ('M', 'F'))
# ch_event_value_set(event_key, event_type, patient_key, date_serviced, code, code_system, name)
#
###
{prompt}
"""


if prompt:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=get_prompt_template(prompt),
        temperature=0,
        max_tokens=250,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["#", ";"]
    )

    output = response["choices"][0]["text"]

    df = snow_session.sql(output)

    st.session_state[StateKey.CHAT_GENERATED].append(output)
    st.session_state[StateKey.CHAT_PAST].append(prompt)
    st.session_state[StateKey.RESULT_DATAFRAME].append(df)

if st.session_state[StateKey.CHAT_GENERATED]:

    for i in range(len(st.session_state[StateKey.CHAT_GENERATED]) - 1, -1, -1):
        st.info(st.session_state[StateKey.CHAT_PAST][i])
        st.code(st.session_state[StateKey.CHAT_GENERATED][i], language="sql")
        st.dataframe(st.session_state[StateKey.RESULT_DATAFRAME][i])
