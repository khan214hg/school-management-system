import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

if not firebase_admin._apps:
    firebase_config = json.loads(st.secrets["firebase_creds"])
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)

db = firestore.client()
