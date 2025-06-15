import streamlit as st
import pandas as pd
import os

FILE_NAME = "parents.csv"

def load_data():
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
    else:
        df = pd.DataFrame(columns=["Parent Name", "Student Name", "Contact", "Relation"])
        df.to_csv(FILE_NAME, index=False)
    return df

def app():
    st.subheader("👨‍👩‍👧‍👦 Parents Management")

    # Load data
    parents_df = load_data()

    # Add new parent
    st.markdown("### Add New Parent Record")
    with st.form("parent_form"):
        parent_name = st.text_input("Parent Name")
        student_name = st.text_input("Student Name")
        contact = st.text_input("Contact Number")
        relation = st.selectbox("Relation", ["Father", "Mother", "Guardian"])
        submitted = st.form_submit_button("Add Parent Record")

        if submitted:
            if parent_name and student_name and contact:
                new_row = {
                    "Parent Name": parent_name,
                    "Student Name": student_name,
                    "Contact": contact,
                    "Relation": relation
                }
                parents_df = pd.concat([parents_df, pd.DataFrame([new_row])], ignore_index=True)
                parents_df.to_csv(FILE_NAME, index=False)
                st.success(f"Parent record added for {parent_name}")
            else:
                st.warning("Please fill all fields.")

    # Show parent records
    st.markdown("### Parent Records")
    st.dataframe(parents_df)

    # Reset parent records
    if st.button("Reset All Parent Records", key="reset_parents"):
        parents_df = pd.DataFrame(columns=["Parent Name", "Student Name", "Contact", "Relation"])
        parents_df.to_csv(FILE_NAME, index=False)
        st.success("All parent records have been reset!")
        st.experimental_rerun()
