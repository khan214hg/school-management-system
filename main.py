import streamlit as st
import dashboard
import admission_management
import student_management
import parents_management
import staff_management

# App config
st.set_page_config(page_title="School Management System", layout="wide")

# Dark / Light theme switcher
theme_mode = st.sidebar.radio("🌗 Select Theme", ["Light", "Dark"])

# Apply theme CSS
if theme_mode == "Dark":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0e1117;
            color: white;
        }
        div[data-testid="stSidebar"] {
            background-color: #161b22;
            color: white;
        }
        label, .css-1cpxqw2, .css-1d391kg {
            color: white !important;
        }
        div[data-testid="stMetricValue"] {
            color: white !important;
        }
        div[data-testid="stMetricLabel"] {
            color: white !important;
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
            color: black;
        }
        div[data-testid="stSidebar"] {
            background-color: #f0f2f6;
            color: black;
        }
        label, .css-1cpxqw2, .css-1d391kg {
            color: black !important;
        }
        div[data-testid="stMetricValue"] {
            color: black !important;
        }
        div[data-testid="stMetricLabel"] {
            color: black !important;
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

# Call modules
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
