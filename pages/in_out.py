import streamlit as st
from models.db_utils import get_items_by_name, record_stock_change

def in_out_page():
    st.title("In/Out Operations")

    item_name = st.text_input("Search Item")
    items = get_items_by_name(item_name)

    if items:
        item_names = [item.name for item in items]
        selected_item_name = st.selectbox("Select Item", item_names)
        selected_item = next(item for item in items if item.name == selected_item_name)

        operation = st.selectbox("Select Operation", ["In", "Out"])
        quantity = st.number_input("Enter Quantity", min_value=0)

        if st.button("Update Stock"):
            if operation == "In":
                record_stock_change(selected_item.id, quantity, "Stock added")
                selected_item.quantity += quantity
                st.success(f"Added {quantity} units to {selected_item.name}.")
            else:
                record_stock_change(selected_item.id, -quantity, "Stock removed")
                selected_item.quantity -= quantity
                st.success(f"Removed {quantity} units from {selected_item.name}.")
            st.experimental_rerun()
    else:
        st.warning("No items found!")
