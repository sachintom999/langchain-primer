from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import ollama


from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

prompt = ChatPromptTemplate.from_messages([

    ("system","you are a helpful assistant. answer the queries"),
    ("user","Question: {question}"),
])


st.title("sample")
input_text = st.text_input("seach...")


llm=ollama()
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question': input_text}))