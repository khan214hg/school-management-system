import streamlit as st

def apply_react_theme():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            color: #e0e0e0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        div[data-testid="stSidebar"] {
            background-color: #1a1a2e;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #00adb5;
        }
        label, .css-1cpxqw2, .css-1d391kg {
            color: #eeeeee !important;
        }
        div[data-testid="stMetricValue"] {
            color: #00adb5 !important;
        }
        button[kind="primary"] {
            background-color: #00adb5 !important;
            color: black !important;
            border-radius: 8px;
            padding: 0.5em 1em;
        }
        button[kind="secondary"] {
            background-color: #393e46 !important;
            color: white !important;
            border-radius: 8px;
            padding: 0.5em 1em;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
