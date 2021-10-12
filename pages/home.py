import streamlit as st

def app():
    #title to home page
    st.header("Welcome to")
    st.title("Object Prediction Model")
    #Image path
    st.image("images/obj.jpg")
    #Simple text to project
    st.write("This model that allows and helps user to predict the object!")
    st.write("""
                1. Installing of OpenCV -> pip install opencv-python
                2. Configuration files -> configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt' AND weightsPath = 'frozen_inference_graph.pb'
                3. Building Model
                4. Calculating Confidence
                """)
    st.write("\n")
    st.write("Till now project completed")
    st.progress(0.9)