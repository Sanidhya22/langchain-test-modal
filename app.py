# Bring in deps
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper


os.environ['OPENAI_API_KEY'] = apikey

topic1 = ''
with open("one.txt", "r") as f:
    topic = f.read().strip()
    # print(topic)
# App framework
st.title('Youtube GPT Helper')
prompt = st.text_input('Plug in your prompt here')

# Prompt templates
transcriptTemplate = PromptTemplate(
    input_variables=['topic'],
    template='this whole Transcript of meeting : {topic}'
)

# script_template = PromptTemplate(
#     input_variables=['title', 'wikipedia_research'],
#     template='write me a youtube video script based on this title TITLE: {title} while leveraging this wikipedia reserch:{wikipedia_research} '
# )

# Memory
title_memory = ConversationBufferMemory(
    input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(
    input_key='title', memory_key='chat_history')


# Llms
llm = OpenAI(temperature=0.9, model_name='gpt-3.5-turbo', max_tokens=256)
title_chain = LLMChain(llm=llm, prompt=transcriptTemplate,
                       verbose=True, output_key='title', memory=title_memory)
# script_chain = LLMChain(llm=llm, prompt=script_template,
#                         verbose=True, output_key='script', memory=script_memory)

# wiki = WikipediaAPIWrapper()

# Show stuff to the screen if there's a prompt
if prompt:
    title = title_chain.run(prompt)
    # wiki_research = wiki.run(prompt)
    # script = script_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title)
    # st.write(script)

    # with st.expander('Title History'):
    #     st.info(title_memory.buffer)

    # with st.expander('Script History'):
    #     st.info(script_memory.buffer)

    # with st.expander('Wikipedia Research'):
    #     st.info(wiki_research)
