import streamlit as st
import json

firebase_config = json.loads(st.secrets["firebase"])
cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred)
db = firestore.client()
