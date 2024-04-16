from openai import OpenAI
import streamlit as st
import json

st.snow()
st.balloons()

st.title("💬An AI Code Reviewer🔍")
st.subheader("by Mustafa Shaik❤️")
code = st.text_area("Enter Your Python Code here...")

if st.button("Generate"):
    f = open('keys/.openai_api_key.txt')
    key = f.read()
    client = OpenAI(api_key = key)

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """ You are a friendly AI assistant. You take a python code as an input from the user. 
             Your job is to explain the bugs and generate the fixed code as an output.
             Your output is a JSON with the following structure:
             {"Bugs": "review_on_code", "Code": '''python_fixed_code'''}
             """},
             {"role": "user", "content": f"fix and explain the bugs in the following python code: {code}"}
        ],
        temperature=0.5
    )

    review = json.loads(response.choices[0].message.content)

    
    st.write(review)

    st.subheader("Code Review")
    st.write(review["Bugs"])
    st.code(review["Code"])