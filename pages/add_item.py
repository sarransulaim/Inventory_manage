import streamlit as st
from models.db_utils import add_item, add_department, get_all_departments

def add_new_item():
    st.title("Add New Item")

    name = st.text_input("Item Name")
    barcode = st.text_input("Barcode")
    quantity = st.number_input("Quantity", min_value=0)
    low_stock_threshold = st.number_input("Low Stock Threshold", min_value=0)

    departments = get_all_departments()
    department_choices = [dept.name for dept in departments]
    department_name = st.selectbox("Select Department", department_choices)

    if st.button("Add Item"):
        department = next((dept for dept in departments if dept.name == department_name), None)
        if department:
            item = add_item(name, barcode, quantity, low_stock_threshold, department.id)
            if isinstance(item, Item):
                st.success(f"Item '{name}' added successfully!")
            else:
                st.error(item)
        else:
            st.error("Department not found!")
