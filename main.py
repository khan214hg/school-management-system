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

# ✅ CSS for pro design
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #e0e0e0;
    padding: 1rem;
}
div[data-testid="stSidebar"] {
    background-color: #1a1a2e;
    padding: 2rem 1rem;
    border-radius: 10px;
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
    background-color: #393e46;
    border-radius: 5px;
    padding: 0.75rem 1rem;
    margin: 0.25rem 0;
    text-decoration: none;
    transition: background 0.3s, color 0.3s;
    font-weight: bold;
}
.custom-nav a:hover {
    background-color: #00adb5;
    color: black;
}
div[data-testid="stMetric"] {
    background-color: #393e46;
    padding: 1rem;
    border-radius: 8px;
}
button {
    background-color: #00adb5 !important;
    color: #000 !important;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-weight: bold;
}
button:hover {
    background-color: #008891 !important;
    color: #fff !important;
}
</style>
""", unsafe_allow_html=True)

# ✅ Sidebar navbar
st.sidebar.markdown('<div class="sidebar-title">School Manager</div>', unsafe_allow_html=True)
st.sidebar.markdown("""
<div class="custom-nav">
<a href="/?nav=Dashboard" target="_self">🏠 Dashboard</a>
<a href="/?nav=Admission" target="_self">📝 Admissions</a>
<a href="/?nav=Student" target="_self">🎓 Students</a>
<a href="/?nav=Parents" target="_self">👨‍👩‍👧‍👦 Parents</a>
<a href="/?nav=Staff" target="_self">👔 Staff</a>
</div>
""", unsafe_allow_html=True)

# ✅ Nav select
query_params = st.query_params
nav = query_params.get("nav", "Dashboard")

st.title("🏫 School Management System")

# ✅ Helper to load data
def load_csv(file_name, default_cols):
    if os.path.exists(file_name):
        return pd.read_csv(file_name)
    return pd.DataFrame(columns=default_cols)

students_df = load_csv("students.csv", ["Name", "Class", "Contact", "Status"])
staff_df = load_csv("staff.csv", ["Name", "Role", "Contact", "Status"])
admissions_df = load_csv("admissions.csv", ["Name", "Class", "Contact", "Status"])

    st.markdown("### 📊 Admissions by Class")
    if not admissions_df.empty:
        class_counts = admissions_df["Class"].value_counts().reset_index()
        class_counts.columns = ["Class", "Count"]
        fig = px.bar(
            class_counts, x="Class", y="Count", color="Class",
            title="Admissions Count by Class",
            labels={"Count": "Number of Admissions"},
            template="plotly_dark"
        )
        fig.update_layout(
            plot_bgcolor="#2c5364",
            paper_bgcolor="#2c5364",
            font_color="#e0e0e0",
            title_font_color="#00adb5"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No admissions data available to display graph.")

# ✅ Load module
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

# ✅ Footer
st.sidebar.markdown("---")
st.sidebar.caption("Powered by Streamlit | Developed by Waris Khan Tareen 😎")
