import streamlit as st
import pandas as pd
import os

def load_admissions():
    if os.path.exists("admissions.csv"):
        return pd.read_csv("admissions.csv")
    else:
        return pd.DataFrame(columns=["Name", "Class", "Contact", "Status"])

def load_students():
    if os.path.exists("students.csv"):
        return pd.read_csv("students.csv")
    else:
        return pd.DataFrame(columns=["Name", "Class", "Roll Number", "Contact"])

def load_staff():
    if os.path.exists("staff.csv"):
        return pd.read_csv("staff.csv")
    else:
        return pd.DataFrame(columns=["Name", "Position", "Contact", "Status"])

def app():
    st.subheader("🏫 Dashboard Overview")

    # Always load latest data
    admissions_df = load_admissions()
    students_df = load_students()
    staff_df = load_staff()

    # Show metrics
    st.metric("Total Admissions", len(admissions_df))
    st.metric("Total Students", len(students_df))
    st.metric("Total Staff", len(staff_df))

    st.markdown("### Recent Admissions")
    st.dataframe(admissions_df.tail(5))

    st.markdown("### Recent Students")
    st.dataframe(students_df.tail(5))

    st.markdown("### Staff Summary")
    st.dataframe(staff_df.tail(5))
