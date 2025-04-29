import streamlit as st
from pages import 1_Add_Item, 2_In_Out, 3_View_Inventory, 4_Retrieve_Item, 5_Trends

def main():
    st.title("Inventory Management System")

    menu = ["Add Item", "In/Out Operations", "View Inventory", "Retrieve Item", "Trends"]
    choice = st.sidebar.selectbox("Select Option", menu)

    if choice == "Add Item":
        1_Add_Item.run()
    elif choice == "In/Out Operations":
        2_In_Out.run()
    elif choice == "View Inventory":
        3_View_Inventory.run()
    elif choice == "Retrieve Item":
        4_Retrieve_Item.run()
    elif choice == "Trends":
        5_Trends.run()

if __name__ == "__main__":
    main()
