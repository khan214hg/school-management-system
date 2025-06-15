import streamlit as st
import dashboard
import admission_management
import student_management
import parents_management
import staff_management
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="School Management System", layout="wide")

# CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #e0e0e0;
    padding: 1rem;
}
div[data-testid="stMetric"] {
    background-color: #393e46;
    padding: 1rem;
    border-radius: 8px;
}
div[data-testid="stSidebar"] {
    background-color: #1a1a2e;
    padding: 2rem 1rem;
}
h1, h2, h3 {
    color: #00adb5;
}
button {
    background-color: #00adb5 !important;
    color: #000 !important;
    border-radius: 8px;
}
button:hover {
    background-color: #008891 !important;
    color: #fff !important;
}
</style>
""", unsafe_allow_html=True)

# Sidebar nav
st.sidebar.markdown('<div style="color:#00adb5; font-size:24px; font-weight:bold; text-align:center;">School Manager</div>', unsafe_allow_html=True)
st.sidebar.markdown("""
<div class="custom-nav">
<a href="/?nav=Dashboard" target="_self">Dashboard</a>
<a href="/?nav=Admission" target="_self">Admissions</a>
<a href="/?nav=Student" target="_self">Students</a>
<a href="/?nav=Parents" target="_self">Parents</a>
<a href="/?nav=Staff" target="_self">Staff</a>
</div>
""", unsafe_allow_html=True)

# Nav
query_params = st.query_params
nav = query_params.get("nav", "Dashboard")

st.title("🏫 School Management System")

# Load data
def load_csv(file_name, default_cols):
    if os.path.exists(file_name):
        return pd.read_csv(file_name)
    return pd.DataFrame(columns=default_cols)

students_df = load_csv("students.csv", ["Name", "Class", "Contact", "Status"])
staff_df = load_csv("staff.csv", ["Name", "Role", "Contact", "Status"])
admissions_df = load_csv("admissions.csv", ["Name", "Class", "Contact", "Status"])

# Dashboard
if nav == "Dashboard":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Students", len(students_df))
    with col2:
        st.metric("Total Staff", len(staff_df))
    with col3:
        st.metric("New Admissions", len(admissions_df))

    st.markdown("### 📊 Admissions by Class")
    if not admissions_df.empty:
        class_counts = admissions_df["Class"].value_counts().reset_index()
        class_counts.columns = ["Class", "Count"]
        fig = px.bar(class_counts, x="Class", y="Count", color="Class",
                     title="Admissions Count by Class")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No admissions data available to display graph.")

# Modules
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
