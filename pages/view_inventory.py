import streamlit as st
import pandas as pd
from models.db_utils import get_inventory

def run():
    st.subheader("Current Inventory")

    items = get_inventory()
    data = [{"Item Name": item.name, "Quantity": item.quantity, "Low Stock Threshold": item.low_stock_threshold} for item in items]
    df = pd.DataFrame(data)

    st.dataframe(df)
  
