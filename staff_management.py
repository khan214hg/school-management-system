import streamlit as st
import pandas as pd
import os

FILE_NAME = "staff.csv"

def load_data():
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
    else:
        df = pd.DataFrame(columns=["Name", "Position", "Contact", "Status"])
        df.to_csv(FILE_NAME, index=False)
    return df

def app():
    st.subheader("👩‍🏫 Staff Management")

    # ✅ Load staff data
    staff_df = load_data()

    # Add new staff member
    st.markdown("### Add New Staff Member")
    with st.form("staff_form"):
        name = st.text_input("Staff Name")
        position = st.text_input("Position")
        contact = st.text_input("Contact Number")
        status = st.selectbox("Status", ["Active", "On Leave", "Resigned"])
        submitted = st.form_submit_button("Add Staff Member")

        if submitted:
            if name and position and contact:
                new_row = {
                    "Name": name,
                    "Position": position,
                    "Contact": contact,
                    "Status": status
                }
                staff_df = pd.concat([staff_df, pd.DataFrame([new_row])], ignore_index=True)
                staff_df.to_csv(FILE_NAME, index=False)
                st.success(f"Staff member {name} added!")
            else:
                st.warning("Please fill all fields.")

    # Show staff records
    st.markdown("### Staff Records")
    st.dataframe(staff_df)

    # Reset button
    if st.button("Reset All Staff Records", key="reset_staff"):
        staff_df = pd.DataFrame(columns=["Name", "Position", "Contact", "Status"])
        staff_df.to_csv(FILE_NAME, index=False)
        st.success("All staff records have been reset!")
        st.experimental_rerun()
