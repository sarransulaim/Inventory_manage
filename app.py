import streamlit as st
from pages import add_item, in_out, view_inventory, retrieve_item, trends

st.set_page_config(page_title="Inventory Manager", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", (
    "Add Item", 
    "IN / OUT", 
    "View Inventory", 
    "Retrieve Item", 
    "Trends & Forecast"
))

if page == "Add Item":
    add_item.render()
elif page == "IN / OUT":
    in_out.render()
elif page == "View Inventory":
    view_inventory.render()
elif page == "Retrieve Item":
    retrieve_item.render()
elif page == "Trends & Forecast":
    trends.render()
