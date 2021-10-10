import streamlit as st
from pages import home, prediction, scope, about

# Configure the web page.
st.set_page_config(
    page_title = 'Object Prediction',
    page_icon = 'images\obj.jpg',
    layout = 'centered',
    initial_sidebar_state = 'auto'
)

#PAGES

pages = {
            "Home": home,
            #"Data Info": data,
            "Prediction": prediction,
            #"Visualization": visualization,
            "Scope": scope,
            #"Model Info": model,
            "About Me": about
        }

#st.title("Welcome")
st.sidebar.title("Object Prediction")
st.sidebar.image("./images/main-qimg-3783b0de7ef92fbd7e1d96a90577f089.png", width=250)


page = st.sidebar.radio("Pages",list(pages.keys()))

pages[page].app()