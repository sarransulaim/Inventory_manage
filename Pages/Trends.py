import streamlit as st
import pandas as pd
import plotly.express as px
from models.db_utils import get_inventory

def run():
    st.subheader("Stock Trends")

    items = get_inventory()
    trend_data = [{"Item Name": item.name, "Quantity": item.quantity} for item in items]
    df = pd.DataFrame(trend_data)

    fig = px.bar(df, x='Item Name', y='Quantity', title="Stock Levels")
    st.plotly_chart(fig)
  
