import streamlit as st
from models.db_utils import get_items_by_name
from prophet import Prophet
import pandas as pd
import numpy as np

def trends_page():
    st.title("Trends and Predictions")

    item_name = st.text_input("Search Item")
    items = get_items_by_name(item_name)

    if items:
        item_names = [item.name for item in items]
        selected_item_name = st.selectbox("Select Item", item_names)
        selected_item = next(item for item in items if item.name == selected_item_name)

        if st.button("Predict"):
            # Example: Generating random data for prediction
            history = get_item_history(selected_item.id)
            if history:
                data = [{"ds": h.timestamp, "y": h.change} for h in history]
                df = pd.DataFrame(data)
                df['ds'] = pd.to_datetime(df['ds'])

                model = Prophet()
                model.fit(df)

                future = model.make_future_dataframe(df, periods=365)  # Predict for 1 year
                forecast = model.predict(future)

                st.write(f"Predicted Trends for {selected_item.name}")
                st.write(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])

                # Make a list of predicted orders for low stock items
                low_stock_items = [item for item in items if item.quantity <= item.low_stock_threshold]
                if low_stock_items:
                    st.write("Predicted Order List for Low Stock Items:")
                    for item in low_stock_items:
                        st.write(f"{item.name}: Order {item.low_stock_threshold - item.quantity} units")
            else:
                st.warning("No stock history found for this item.")
    else:
        st.warning("No items found!")
