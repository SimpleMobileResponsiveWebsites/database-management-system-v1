import streamlit as st
import pandas as pd
import numpy as np
import sqlalchemy as sa
from datetime import datetime, timedelta
import base64

# Set random seed for reproducibility
np.random.seed(42)

# Function to generate test data
def generate_test_data(num_records=1000):
    # Generate brands data
    brands_data = {
        'brand_id': range(1, 21),
        'brand_name': [f'Brand_{i}' for i in range(1, 21)]
    }
    brands_df = pd.DataFrame(brands_data)

    # Generate categories data
    categories_data = {
        'category_id': range(1, 11),
        'category_name': [f'Category_{i}' for i in range(1, 11)]
    }
    categories_df = pd.DataFrame(categories_data)

    # Generate products data
    products_data = {
        'product_id': range(1, num_records + 1),
        'product_name': [f'Product_{i}' for i in range(1, num_records + 1)],
        'brand_id': np.random.randint(1, 21, num_records),
        'category_id': np.random.randint(1, 11, num_records),
        'model_year': np.random.randint(2020, 2024, num_records),
        'list_price': np.random.uniform(10.0, 1000.0, num_records).round(2)
    }
    products_df = pd.DataFrame(products_data)

    # Generate customers data
    customers_data = {
        'customer_id': range(1, 501),
        'first_name': [f'FirstName_{i}' for i in range(1, 501)],
        'last_name': [f'LastName_{i}' for i in range(1, 501)],
        'phone': [f'555-0{str(i).zfill(3)}' for i in range(1, 501)],
        'email': [f'customer_{i}@example.com' for i in range(1, 501)],
        'street': [f'Street_{i}' for i in range(1, 501)],
        'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], 500),
        'state': np.random.choice(['NY', 'CA', 'IL', 'TX', 'AZ'], 500),
        'zip_code': np.random.randint(10000, 99999, 500)
    }
    customers_df = pd.DataFrame(customers_data)

    # Generate stores data
    stores_data = {
        'store_id': range(1, 51),
        'store_name': [f'Store_{i}' for i in range(1, 51)],
        'phone': [f'555-1{str(i).zfill(3)}' for i in range(1, 51)],
        'email': [f'store_{i}@example.com' for i in range(1, 51)],
        'street': [f'Store_Street_{i}' for i in range(1, 51)],
        'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], 50),
        'state': np.random.choice(['NY', 'CA', 'IL', 'TX', 'AZ'], 50),
        'zip_code': np.random.randint(10000, 99999, 50)
    }
    stores_df = pd.DataFrame(stores_data)

    # Generate staffs data
    staffs_data = {
        'staff_id': range(1, 101),
        'first_name': [f'Staff_FirstName_{i}' for i in range(1, 101)],
        'last_name': [f'Staff_LastName_{i}' for i in range(1, 101)],
        'email': [f'staff_{i}@example.com' for i in range(1, 101)],
        'phone': [f'555-2{str(i).zfill(3)}' for i in range(1, 101)],
        'active': np.random.choice([0, 1], 100),
        'store_id': np.random.randint(1, 51, 100),
        'manager_id': [None if i % 10 == 0 else np.random.randint(1, 101) for i in range(1, 101)]
    }
    staffs_df = pd.DataFrame(staffs_data)

    # Generate orders data
    start_date = datetime(2023, 1, 1)
    orders_data = {
        'order_id': range(1, num_records + 1),
        'customer_id': np.random.randint(1, 501, num_records),
        'order_status': np.random.choice(['Pending', 'Processing', 'Shipped', 'Delivered'], num_records),
        'order_date': [start_date + timedelta(days=x) for x in range(num_records)],
        'required_date': [start_date + timedelta(days=x + 7) for x in range(num_records)],
        'shipped_date': [start_date + timedelta(days=x + 3) for x in range(num_records)],
        'store_id': np.random.randint(1, 51, num_records),
        'staff_id': np.random.randint(1, 101, num_records)
    }
    orders_df = pd.DataFrame(orders_data)

    # Generate order_items data
    order_items_data = {
        'order_id': np.repeat(range(1, num_records + 1), 3),  # Each order has 3 items
        'item_id': np.tile(range(1, 4), num_records),
        'product_id': np.random.randint(1, num_records + 1, num_records * 3),
        'quantity': np.random.randint(1, 5, num_records * 3),
        'list_price': np.random.uniform(10.0, 1000.0, num_records * 3).round(2),
        'discount': np.random.choice([0.0, 0.1, 0.2], num_records * 3)
    }
    order_items_df = pd.DataFrame(order_items_data)

    return {
        'brands': brands_df,
        'categories': categories_df,
        'products': products_df,
        'customers': customers_df,
        'stores': stores_df,
        'staffs': staffs_df,
        'orders': orders_df,
        'order_items': order_items_df
    }

# Function to convert DataFrame to CSV for download
def create_download_link(df, filename):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'Download {filename}'
    return href

# Main Streamlit application
def main():
    st.set_page_config(page_title="Database Management System", layout="wide")
    st.title("Database Management System")

    st.header("Download Sample Data")
    num_records = st.number_input("Number of records to generate", min_value=10, max_value=1000, value=100, step=10)
    
    if st.button("Generate Sample Data"):
        sample_data = generate_test_data(num_records)
        
        # Create download buttons for each table
        for table_name, df in sample_data.items():
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label=f"Download {table_name}.csv",
                data=csv,
                file_name=f"{table_name}.csv",
                mime="text/csv"
            )
            st.write(f"Preview of {table_name} dataset:")
            st.dataframe(df.head())
            st.write("---")
    
    st.header("Upload Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Preview of uploaded data:")
        st.dataframe(data.head())
        
        table_name = st.selectbox("Select a table to upload data to", list(sample_data.keys()))
        
        if st.button("Upload to Database"):
            try:
                engine = sa.create_engine('sqlite:///database.db')
                data.to_sql(table_name, engine, if_exists='append', index=False)
                st.success(f"Data uploaded to the {table_name} table successfully!")
            except Exception as e:
                st.error(f"Error uploading data: {e}")

if __name__ == "__main__":
    main()
