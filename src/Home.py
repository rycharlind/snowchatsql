import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from snowchatsql.c_state import CState

st.set_page_config(layout='wide')
st.title('Welcome to SnowChatSQL!')
st.snow()

st.markdown("""
SnowChatSQL allows you to chat with your database using natural language. 
It uses OpenAI's ***text-davinci-003*** model to generate SQL queries based on your input.
""")
         
st.markdown("""
This app is a POC on the ability to analyze any dataset that is stored in a Snowflake database using AI and natural language. 
I used a free sample dataset from the Snowflake Marketplace on Amazon Vendor Analytics.

Before running the app, you must first initialize the vector store with documents from the Snowflake database schema. 
To do this, run the following command from the root directory of the project: `python src/init_vector_store.py`

### Snowflake Sample Dataset: Amazon Vendor Analytics

https://app.snowflake.com/marketplace/listing/GZTYZ3HT1R1/reason-automation-amazon-vendor-analytics-sample-dataset

## Sample Prompts
The below prompts we're generated using `python src/prompt_generator.py` and are based on the sample dataset.
""")
         
b1p = "What is the average revenue per customer?"
b2p = "What is the total return on advertising spend across all campaigns?"
b3p = "What is the average click-through rate across all campaigns?"
b4p = "What is the total number of payments made to vendors?"
b5p = "What is the total number of products in the catalog?"

b1 = st.button(b1p)
b2 = st.button(b2p)
b3 = st.button(b3p)
b4 = st.button(b4p)
b5 = st.button(b5p)

if b1:
    st.session_state[CState.CHAT_PROMPT] = b1p
    switch_page("ChatSQL")

if b2:
    st.session_state[CState.CHAT_PROMPT] = b2p
    switch_page("ChatSQL")

if b3:
    st.session_state[CState.CHAT_PROMPT] = b3p
    switch_page("ChatSQL")

if b4:
    st.session_state[CState.CHAT_PROMPT] = b4p
    switch_page("ChatSQL")

if b5:
    st.session_state[CState.CHAT_PROMPT] = b5p
    switch_page("ChatSQL")

