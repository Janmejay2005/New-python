
import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is my first Streamlit app.")

number = st.slider("Pick a number", 0, 100)
st.write(f"You picked: {number}")

