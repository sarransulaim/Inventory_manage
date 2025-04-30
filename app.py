import streamlit as st
from pages import add_item, in_out, view_inventory, retrieve_item, trends

def main():
    st.title("Inventory Management System")

    menu = ["Add Item", "In/Out Operations", "View Inventory", "Retrieve Item", "Trends"]
    choice = st.sidebar.selectbox("Select Option", menu)

    if choice == "Add Item":
       add_item.run()
    elif choice == "In/Out Operations":
       in_out.run()
    elif choice == "View Inventory":
       view_inventory.run()
    elif choice == "Retrieve Item":
       retrieve_item.run()
    elif choice == "Trends":
       trends.run()

if __name__ == "__main__":
    main()
