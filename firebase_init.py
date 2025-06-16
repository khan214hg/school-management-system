import streamlit as st
import firebase_admin
from firebase_admin import credentials, db

# Load service account (Streamlit secrets ya direct file ka path)
cred = credentials.Certificate("serviceaccountkey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-id.firebaseio.com'
})
