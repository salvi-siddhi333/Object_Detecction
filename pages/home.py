import streamlit as st


def app():
    #title to home page
    st.header("Welcome to")
    st.title("Object Prediction")
    #Image path
    st.image("./images/obj.jpg")
    #Simple text to project
    st.write("This model that allows and helps user to predict the object!")