import streamlit as st
import pandas as pd
import os

FILE_NAME = "students.csv"

def load_data():
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
    else:
        df = pd.DataFrame(columns=["Name", "Class", "Roll Number", "Contact"])
        df.to_csv(FILE_NAME, index=False)
    return df

def app():
    st.subheader("🎒 Student Management")

    # Load data
    students_df = load_data()

    # Add new student
    st.markdown("### Add New Student")
    with st.form("student_form"):
        name = st.text_input("Student Name")
        student_class = st.selectbox("Class", ["Nursery", "KG", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        roll_number = st.text_input("Roll Number")
        contact = st.text_input("Contact Number")
        submitted = st.form_submit_button("Add Student")

        if submitted:
            if name and roll_number and contact:
                new_row = {
                    "Name": name,
                    "Class": student_class,
                    "Roll Number": roll_number,
                    "Contact": contact
                }
                students_df = pd.concat([students_df, pd.DataFrame([new_row])], ignore_index=True)
                students_df.to_csv(FILE_NAME, index=False)
                st.success(f"Student {name} added!")
                st.experimental_rerun()
            else:
                st.warning("Please fill all fields.")

    # Show student records
    st.markdown("### Student Records")
    st.dataframe(students_df)

    # Reset student records
    if st.button("Reset All Student Records", key="reset_students"):
        students_df = pd.DataFrame(columns=["Name", "Class", "Roll Number", "Contact"])
        students_df.to_csv(FILE_NAME, index=False)
        st.success("All student records have been reset!")
        st.experimental_rerun()
