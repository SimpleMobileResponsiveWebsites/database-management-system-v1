import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)

def generate_test_data(num_records=1000):
    # Generate brands data
    brands_data = {
        'brand_id': range(1, 21),
        'brand_name': [f'Brand_{i}' for i in range(1, 21)]
    }
    brands_df = pd.DataFrame(brands_data)
    brands_df.to_csv('brands.csv', index=False)

    # Generate categories data
    categories_data = {
        'category_id': range(1, 11),
        'category_name': [f'Category_{i}' for i in range(1, 11)]
    }
    categories_df = pd.DataFrame(categories_data)
    categories_df.to_csv('categories.csv', index=False)

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
    products_df.to_csv('products.csv', index=False)

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
    customers_df.to_csv('customers.csv', index=False)

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
    stores_df.to_csv('stores.csv', index=False)

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
    staffs_df.to_csv('staffs.csv', index=False)

    # Generate orders data
    start_date = datetime(2023, 1, 1)
    orders_data = {
        'order_id': range(1, num_records + 1),
        'customer_id': np.random.randint(1, 501, num_records),
        'order_status': np.random.choice(['Pending', 'Processing', 'Shipped', 'Delivered'], num_records),
        'order_date': [start_date + timedelta(days=x) for x in range(num_records)],
        'required_date': [start_date + timedelta(days=x+7) for x in range(num_records)],
        'shipped_date': [start_date + timedelta(days=x+3) for x in range(num_records)],
        'store_id': np.random.randint(1, 51, num_records),
        'staff_id': np.random.randint(1, 101, num_records)
    }
    orders_df = pd.DataFrame(orders_data)
    orders_df.to_csv('orders.csv', index=False)

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
    order_items_df.to_csv('order_items.csv', index=False)

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

if __name__ == "__main__":
    # Generate test data with 1000 records
    test_data = generate_test_data(1000)
    print("Test data files have been generated successfully!")
    
    # Print sample counts
    for table_name, df in test_data.items():
        print(f"{table_name}: {len(df)} records")
