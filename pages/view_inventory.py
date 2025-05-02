import streamlit as st
from models.db_utils import get_items_by_name

def view_inventory_page():
    st.title("View Inventory")

    item_name = st.text_input("Search Item")
    items = get_items_by_name(item_name)

    if items:
        st.write("Inventory Details:")
        for item in items:
            st.write(f"Name: {item.name}, Barcode: {item.barcode}, Quantity: {item.quantity}")
    else:
        st.warning("No items found!")
