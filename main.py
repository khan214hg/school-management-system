import streamlit as st
import dashboard
import admission_management
import student_management
import parents_management
import staff_management

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
