import streamlit as st

def display_input_form(label, input_type="text", **kwargs):
    if input_type == "text":
        return st.text_input(label, **kwargs)
    elif input_type == "number":
        return st.number_input(label, **kwargs)
    elif input_type == "select":
        return st.selectbox(label, **kwargs)
      
