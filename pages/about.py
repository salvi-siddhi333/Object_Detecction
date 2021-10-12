"""This create About me page"""

# Import necessary module
from typing import Text
from six import text_type
import streamlit as st

def app():
    st.balloons()
    st.title('Contact Us')
    st.markdown('''#### Name:
    Salvi Siddhi''')
    st.markdown('''#### Email:
    siddhi.salvi@sakec.ac.in''')
    #with st.echo():
    st.markdown('''<p>
                    <h4>GitHub:</h4>
                    <div style="background: rgb(248, 249, 251);border-radius: 0.25rem;, height: 50px">
                        <p style="padding:10px">
                            <a href = "https://github.com/salvi-siddhi333/Object_Detection" 
                                        target="_blank"
                                        style="text-decoration:None; 
                                            color:black;
                                            padding:1rem;
                                            font-family:'Courier New';"> 
                                        You can find my project here!
                            </a>
                        </p>
                    </div>
                    </p>''', unsafe_allow_html=True)