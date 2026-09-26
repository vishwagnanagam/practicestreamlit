import streamlit as st
st.title("Welcome! Ai Chatbot.")
prompt = st.text_input("Enter the prompt:")
if st.button("send"):
    if prompt:
        st.write(prompt)
        st.success("success")
    else:
        st.warning("please enter correct prompt")
