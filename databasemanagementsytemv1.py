import streamlit as st
import sqlalchemy as sa
import pandas as pd
from io import StringIO

# Connect to the SQLite database
engine = sa.create_engine('sqlite:///database.db')

def main():
    st.set_page_config(page_title="Database Management System", layout="wide")
    st.title("Database Management System")

    # Display the database schema
    st.subheader("Database Schema")
    try:
        with open("database_schema.png", "rb") as f:
            schema_image = f.read()
        st.image(schema_image, use_column_width=True)
    except FileNotFoundError:
        st.error("Database schema image not found.")

    # Allow user to upload data
    st.subheader("Upload Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        # Read the uploaded file into a DataFrame
        data = pd.read_csv(uploaded_file)

        # Ask the user which table to upload the data to
        table_name = st.selectbox("Select a table to upload data to", get_table_names(engine))

        if st.button("Upload Data"):
            try:
                # Write the DataFrame to the selected table
                data.to_sql(table_name, engine, if_exists='append', index=False)
                st.success(f"Data uploaded to the {table_name} table successfully!")
            except Exception as e:
                st.error(f"Error uploading data: {e}")

    # Allow user to query the database
    st.subheader("Query the Database")
    query = st.text_area("Enter your SQL query:", height=200)
    if st.button("Run Query"):
        try:
            # Execute the query and display the results
            result = pd.read_sql_query(query, engine)
            st.dataframe(result)
        except Exception as e:
            st.error(f"Error executing the query: {e}")

def get_table_names(engine):
    """
    Get the names of all tables in the database.
    """
    inspector = sa.inspect(engine)
    return inspector.get_table_names()

if __name__ == "__main__":
    main()
