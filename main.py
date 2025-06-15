import streamlit as st
import dashboard
import admission_management
import student_management
import parents_management
import staff_management

st.set_page_config(page_title="School Management System", layout="wide")

# Apply React-style CSS
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    div[data-testid="stSidebar"] {
        background-color: #1a1a2e;
        padding-top: 2rem;
    }
    .sidebar-title {
        color: #00adb5;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .custom-nav {
        display: flex;
        flex-direction: column;
    }
    .custom-nav a {
        color: #eeeeee;
        padding: 0.75rem 1rem;
        margin: 0.25rem 0;
        text-decoration: none;
        border-radius: 5px;
        background-color: #393e46;
        transition: background 0.3s;
    }
    .custom-nav a:hover {
        background-color: #00adb5;
        color: black;
    }
    button[kind="primary"] {
        background-color: #00adb5 !important;
        color: black !important;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    h1, h2, h3 {
        color: #00adb5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navbar
st.sidebar.markdown('<div class="sidebar-title">School Manager</div>', unsafe_allow_html=True)
st.sidebar.markdown(
    """
    <div class="custom-nav">
        <a href="/?nav=Dashboard" target="_self">Dashboard</a>
        <a href="/?nav=Admission" target="_self">Admissions</a>
        <a href="/?nav=Student" target="_self">Students</a>
        <a href="/?nav=Parents" target="_self">Parents</a>
        <a href="/?nav=Staff" target="_self">Staff</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Get nav selection from URL (modern API)
query_params = st.query_params
nav = query_params.get("nav", "Dashboard")

st.title("🏫 School Management System")

# Load module based on nav
if nav == "Dashboard":
    dashboard.app()
elif nav == "Admission":
    admission_management.app()
elif nav == "Student":
    student_management.app()
elif nav == "Parents":
    parents_management.app()
elif nav == "Staff":
    staff_management.app()

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Powered by Streamlit | Developed by Waris Khan Tareen 😎")
