from ctypes import alignment
import streamlit as st

def app():
    st.title("Scope for Object Detection")

    st.write("""
        Object detection in images and video has received lots of attention in the computer vision 
        and pattern recognition communities over recent years. We have had great progress in the field, 
        processing a single image used to take 20 seconds per image and today it takes less than 20 milliseconds.
    """)
    col1, col2, col3 = st.columns([2,6,2])

    with col1:
        st.write("")

    with col2:
        st.image("images\object-detection-01.jpg", width=300)

    with col3:
        st.write("")

    st.write("""
        Of the problems related to these fields, analyzing an image and recognizing all objects remains to be 
        one of the most challenging ones.
        For humans and many other animals, visual perception is one of the most important senses; we heavily rely 
        on vision whenever we interact with our environment. In order to pick up a glass, we need to first determine 
        which part of our visual impression corresponds to the glass before we can find out where we have to move our 
        hands in order to grasp it.
        The same code that can be used to recognize Stop signs or pedestrians in a self driving vehicle signs can 
        also be used to find cancer cells in a tissue biopsy.
        If we want to recognize another human, we first have to find out which part of the image we see represents 
        that individual, as well as any distinguishing factors of their face.
        Notably, we generally do not actively consider these basic steps, but these steps pose a major challenge 
        for artificial systems dealing with image processing.
    """)