
import streamlit as st

st.title("Hello Streamlit with Ngrok!")
st.write("This is a simple Streamlit application running through Ngrok.")
st.slider("Select a value:", 0, 100, 50)
