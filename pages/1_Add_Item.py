import streamlit as st
from utils.ui_helpers import display_input_form
from models.db_utils import add_item
from models.db_utils import get_inventory

def run():
    st.subheader("Add New Item")

    with st.form(key='add_item_form'):
        item_name = st.text_input("Item Name")
        barcode = st.text_input("Barcode (manual input or scan)")
        quantity = st.number_input("Initial Quantity", min_value=0)
        low_stock = st.number_input("Low Stock Threshold", min_value=1)
        department = st.selectbox("Department", ["Select Department", "Electronics", "Furniture", "Clothing"])  # Adjust as needed
        submit = st.form_submit_button("Add Item")

        if submit:
            if item_name and barcode:
                add_item(item_name, barcode, quantity, low_stock, department)
                st.success("Item Added!")
            else:
                st.error("Please provide all required fields")

