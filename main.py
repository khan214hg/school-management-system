import streamlit as st
import dashboard
import admission_management
import student_management
import parents_management
import staff_management

# App config
st.set_page_config(page_title="School Management System", layout="wide")

# React-style theme apply (no theme switcher)
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    div[data-testid="stSidebar"] {
        background-color: #1a1a2e;
        color: #e0e0e0;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #00adb5;
    }
    label, .css-1cpxqw2, .css-1d391kg {
        color: #eeeeee !important;
    }
    div[data-testid="stMetricValue"] {
        color: #00adb5 !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #00adb5 !important;
    }
    button[kind="primary"] {
        background-color: #00adb5 !important;
        color: black !important;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    button[kind="secondary"] {
        background-color: #393e46 !important;
        color: white !important;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("🏫 School Management System")

# Sidebar menu
menu = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "Admission Management",
        "Student Management",
        "Parents Management",
        "Staff Management"
    ]
)

# Load module
if menu == "Dashboard":
    dashboard.app()
elif menu == "Admission Management":
    admission_management.app()
elif menu == "Student Management":
    student_management.app()
elif menu == "Parents Management":
    parents_management.app()
elif menu == "Staff Management":
    staff_management.app()

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Powered by Streamlit | Developed by Waris Khan Tareen 😎")
