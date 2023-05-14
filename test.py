# Bring in deps
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper
from langchain.prompts import PromptTemplate

os.environ['OPENAI_API_KEY'] = apikey

# Load topic from file
with open("one.txt", "r") as f:
    topic = f.read().strip()
    # print(topic)

# App framework
st.title('Youtube GPT Helper')
prompt = st.text_input('Plug in your prompt here')

# Create LLMChain object and generate response
llm = OpenAI()
llmChain = LLMChain(
    llm=llm, prompt=PromptTemplate(input_variables=['topic'], template="Summerize this whole Transcript of meeting : {topic}"), output_key='text')
response = llmChain.generate()
st.write(response)
print(response)
