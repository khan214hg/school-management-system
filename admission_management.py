import streamlit as st
import pandas as pd
import os

FILE_NAME = "admissions.csv"

def load_data():
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
    else:
        df = pd.DataFrame(columns=["Name", "Class", "Contact", "Status"])
        df.to_csv(FILE_NAME, index=False)
    return df

def app():
    st.subheader("📌 Admission Management")

    # Load data
    admissions_df = load_data()

    # Add new admission
    st.markdown("### Add New Admission")
    with st.form("admission_form"):
        name = st.text_input("Student Name")
        student_class = st.selectbox("Class", ["Nursery", "KG", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        contact = st.text_input("Contact Number")
        submitted = st.form_submit_button("Add Admission")

        if submitted:
            if name and contact:
                new_row = {"Name": name, "Class": student_class, "Contact": contact, "Status": "Pending"}
                admissions_df = pd.concat([admissions_df, pd.DataFrame([new_row])], ignore_index=True)
                admissions_df.to_csv(FILE_NAME, index=False)
                st.success(f"Admission added for {name}")
                st.experimental_rerun()
            else:
                st.warning("Please fill in all fields.")

    # Show existing admissions
    st.markdown("### Current Admissions")
    st.dataframe(admissions_df)

    # Reset admissions
    if st.button("Reset All Admissions", key="reset_admission"):
        admissions_df = pd.DataFrame(columns=["Name", "Class", "Contact", "Status"])
        admissions_df.to_csv(FILE_NAME, index=False)
        st.success("All admissions have been reset!")
        st.experimental_rerun()
