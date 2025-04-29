import streamlit as st
from pages import Add_Item, In_Out, ViewInventory, Retrieve_Item, Trends

def main():
    st.title("Inventory Management System")

    menu = ["Add Item", "In/Out Operations", "View Inventory", "Retrieve Item", "Trends"]
    choice = st.sidebar.selectbox("Select Option", menu)

    if choice == "Add Item":
        Add_Item.run()
    elif choice == "In/Out Operations":
        In_Out.run()
    elif choice == "View Inventory":
        View_Inventory.run()
    elif choice == "Retrieve Item":
        Retrieve_Item.run()
    elif choice == "Trends":
        Trends.run()

if __name__ == "__main__":
    main()
  
