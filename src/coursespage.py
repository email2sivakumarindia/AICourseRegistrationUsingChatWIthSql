from langchain_community.utilities import SQLDatabase
import streamlit as st
import mysql.connector
from mysql.connector import Error
from urllib.parse import quote_plus

def get_db_connection():
    """Create and return a database connection"""
    password = "Welcome@1"  # Example password with special characters
    encoded_password = quote_plus(password)  # Encodes '@' -> '%40', '!' -> '%21'

    try:
        connection = mysql.connector.connect(
            host= "localhost",
            database="testsqlai",
            user="root",
            password=password,
            port= 3306
        )
        return connection
    except Error as e:
        st.error(f"Database connection error: {e}")
        return None


def fetch_table_data(table_name):
    """Fetch data from specified table"""
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 50")  # Safety limit
            rows = cursor.fetchall()

            # Get column names
            if rows:
                columns = list(rows[0].keys())
                return rows, columns
            return None, None
        except Error as e:
            st.error(f"Error fetching data: {e}")
            return None, None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


def display_row_in_tab(row, columns, index):
    """Display a single row in a tab"""
    with st.expander("row[1]", expanded=index == 0):
        col1, col2 = st.columns(2)

        with col1:
            for col in columns:
                st.write(f"**{col}:**", row[col])

        with col2:
            st.subheader("Raw Data")
            st.json(row)


def load(db: SQLDatabase):
    st.set_page_config(page_title="Row Tab Viewer", layout="wide")
    st.title("🔍 SQL Row Explorer")

    # Table selection
   # table_name = st.text_input("Enter table name:")
    table_name = "courses"

    if table_name:
        rows, columns = fetch_table_data(table_name)

        if rows:
            #st.success(f"Found {len(rows)} rows in table '{table_name}'")

            # Display each row in its own expandable section
            for i, row in enumerate(rows):
                display_row_in_tab(row, columns, i)

            # Summary stats
            st.divider()
            #st.subheader("Table Summary")
            #st.write(f"Total rows displayed: {len(rows)}")
            #st.write(f"Columns: {', '.join(columns)}")
        else:
            st.warning(f"No data found in table '{table_name}'")