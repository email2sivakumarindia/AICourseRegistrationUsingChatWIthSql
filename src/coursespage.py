from langchain_community.utilities import SQLDatabase
import streamlit as st
import mysql.connector
from mysql.connector import Error
from urllib.parse import quote_plus
from datetime import datetime

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


def display_course_info(row):
    st.title(row['course_name'])

    # Create columns for better layout
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("data:image/jpeg;base64,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",
                caption="Course Image", use_container_width=True)

        st.write("Price",  row["price"])
        st.write("Duration", row["duration_weeks"])
        st.write("Location", row["location"])
        st.write("Available Seats", row['max_students'])

    with col2:
        st.header("Course Description")
        st.write(row['course_description'])

        st.divider()

        st.subheader("Schedule")
        st.write(f"**Start Date:**" + row['start_date'].strftime("%Y-%m-%d %H:%M:%S"))
        st.write(f"**End Date:**" + row['end_date'].strftime("%Y-%m-%d %H:%M:%S"))

        st.divider()

        st.subheader("Instructor Information")
        st.write("**Name:** " + row['instructor_name'])
        st.write("**Email:** " + row['email'])
        st.write("**Phone:**" + row['phone_number'])

    # Add a registration button
    #if st.button("Enroll Now", type="primary", use_container_width=True):
       #st.success("Registration form will appear here!")

def display_row_in_tab(row, columns, index):
    """Display a single row in a tab"""
    with st.expander(row["course_name"], expanded=index == 0):
        display_course_info(row)



def load():
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