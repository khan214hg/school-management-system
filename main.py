import streamlit as st
import dashboard
import admission_management
import student_management
import parents_management
import staff_management

st.set_page_config(page_title="School Management System", layout="wide")

# Apply React-style polished CSS
st.markdown(
    """
    <style>
    /* App background + font */
    .stApp {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #e0e0e0;
        padding: 1rem;
    }

    /* Sidebar styling */
    div[data-testid="stSidebar"] {
        background-color: #1a1a2e;
        padding-top: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
        color: #e0e0e0;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #00adb5;
        margin-bottom: 0.5rem;
    }

    /* General text elements */
    p, span, div, li, label {
        color: #000000 !important;
    }

    /* Metrics */
    div[data-testid="stMetricValue"], div[data-testid="stMetricLabel"] {
        color: #00adb5 !important;
    }

    /* Buttons */
    button {
        background-color: #00adb5 !important;
        color: #000000 !important;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        border: none;
        transition: background 0.3s, color 0.3s;
    }
    button:hover {
        background-color: #008891 !important;
        color: #ffffff !important;
    }

    /* Sidebar navbar links */
    .sidebar-title {
        color: #000000;
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
        background-color: #393e46;
        border-radius: 5px;
        padding: 0.75rem 1rem;
        margin: 0.25rem 0;
        text-decoration: none;
        transition: background 0.3s, color 0.3s;
    }
    .custom-nav a:hover {
        background-color: #00adb5;
        color: black;
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

# Get nav selection
query_params = st.query_params
nav = query_params.get("nav", "Dashboard")

st.title("🏫 School Management System")

# Load module
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
