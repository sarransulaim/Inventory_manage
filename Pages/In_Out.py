import streamlit as st
from models.db_utils import get_item_by_name, update_stock

def run():
    st.subheader("Stock In/Out")

    item_name = st.text_input("Search Item Name")
    if item_name:
        items = get_item_by_name(item_name)
        if items:
            selected_item = st.selectbox("Select Item", [item.name for item in items])
            action = st.selectbox("Choose Action", ["IN", "OUT"])

            quantity = st.number_input("Quantity to Update", min_value=1)

            if st.button("Update Stock"):
                item = next(item for item in items if item.name == selected_item)
                if action == "IN":
                    update_stock(item.id, quantity)
                    st.success(f"Added {quantity} to {selected_item}")
                elif action == "OUT":
                    update_stock(item.id, -quantity)
                    st.success(f"Subtracted {quantity} from {selected_item}")
                  
