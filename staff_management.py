import streamlit as st
import pandas as pd
import os

FILE_NAME = "staff.csv"

# Check file or create if not exists
if os.path.exists(FILE_NAME):
    staff_df = pd.read_csv(FILE_NAME)
else:
    staff_df = pd.DataFrame(columns=["Name", "Position", "Contact", "Status"])
    staff_df.to_csv(FILE_NAME, index=False)

def app():
    st.subheader("👩‍🏫 Staff Management")

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
                st.experimental_rerun()
            else:
                st.warning("Please fill all fields.")

    # Show staff records
    st.markdown("### Staff Records")
    st.dataframe(staff_df)

    # Reset staff records
    if st.button("Reset All Staff Records", key="reset_staff"):
        staff_df = pd.DataFrame(columns=["Name", "Position", "Contact", "Status"])
        staff_df.to_csv(FILE_NAME, index=False)
        st.success("All staff records have been reset!")
        st.experimental_rerun()
