"""This create About me page"""

# Import necessary module
from typing import Text
from six import text_type
import streamlit as st

def app():
    st.balloons()
    st.title('Contact Us')
    st.markdown('''### Name:
    Salvi Siddhi''')
    st.markdown('''### Email:
    siddhi.salvi@sakec.ac.in''')
    st.markdown('''### GitHub: [Salvi Siddhi](https://github.com/salvi-siddhi333/)''')