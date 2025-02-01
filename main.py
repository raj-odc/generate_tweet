import streamlit as st

import os

os.environ['GOOGLE_API_KEY']  = "AIzaSyBVKO64abIwVDTdvJZHKJy5CqNNlps9hnM"
# Using Google Models (Gemini Pro)
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain import PromptTemplate

# Create prompt template for generating tweets

tweet_template = "Give me {number} tweets on {topic}"

tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")


from langchain import LLMChain


# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model



st.header("Tweet Generator")
st.subheader("Generate tweets using Generative AI")

topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value=1,max_value=10, value=1, step=1)

if st.button("Generate"):
    tweets = tweet_chain.invoke({"number": number, "topic": topic})
    st.write(tweets.content)
