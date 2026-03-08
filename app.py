import streamlit as st

st.title("Fake News Detection App")

user_input = st.text_area("Enter a news article")

if st.button("Predict"):
    if user_input:
        st.write("Prediction: Fake / Real (model will go here)")
    else:
        st.write("Please enter some text")
