import streamlit as st

def app():
    st.subheader("📊 Dashboard Overview")

    # Example metrics
    st.metric(label="Total Students", value="1200", delta="+50 this month")
    st.metric(label="Total Staff", value="85", delta="+2 this month")
    st.metric(label="Pending Admissions", value="15", delta="-3 since last week")

    # Example charts placeholder
    st.markdown("### Attendance Summary")
    st.progress(0.75)  # 75% attendance today

    st.markdown("### Fee Collection Status")
    st.progress(0.60)  # 60% fees collected this month

    # Example info cards
    st.info("💡 Tip: Use the sidebar to navigate through management modules.")

    # Columns example
    col1, col2 = st.columns(2)
    with col1:
        st.success("Upcoming event: Science Fair on 25th Sept")
    with col2:
        st.warning("Reminder: Staff meeting tomorrow at 10 AM")
