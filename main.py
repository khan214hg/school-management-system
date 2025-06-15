import streamlit as st
import dashboard
import admission_management
import student_management
import parents_management
import staff_management

import streamlit as st

def theme_switcher():
    theme = st.sidebar.radio("🌗 Select Theme Mode", ["Light", "Dark"])
    if theme == "Dark":
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #0e1117;
                color: #ffffff;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #ffffff;
                color: #000000;
            }
            </style>
            """,
            unsafe_allow_html=True
        )


# App title
st.set_page_config(page_title="School Management System", layout="wide")
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
st.sidebar.caption("Powered by Streamlit | Developed by Waris Khan Tareen😎")
