import streamlit as st
from models.db_utils import get_item_by_name

def run():
    st.subheader("Retrieve Item Information")

    item_name = st.text_input("Enter Item Name")
    if item_name:
        items = get_item_by_name(item_name)
        if items:
            selected_item = st.selectbox("Select Item", [item.name for item in items])
            item = next(item for item in items if item.name == selected_item)
            st.write(f"Item: {item.name}")
            st.write(f"Quantity: {item.quantity}")
            st.write(f"Low Stock Threshold: {item.low_stock_threshold}")
        else:
            st.warning("No item found")
          
