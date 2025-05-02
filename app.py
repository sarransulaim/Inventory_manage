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
    add_item.add_new_item()
elif page == "IN / OUT":
    in_out.handle_in_out()
elif page == "View Inventory":
    view_inventory.display_inventory()
elif page == "Retrieve Item":
    retrieve_item.retrieve_item_info()
elif page == "Trends & Forecast":
    trends.show_trends()
