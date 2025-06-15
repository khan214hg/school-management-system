import streamlit as st
import pandas as pd
import os

def load_admissions():
    if os.path.exists("admissions.csv"):
        return pd.read_csv("admissions.csv")
    else:
        return pd.DataFrame(columns=["Name", "Class", "Contact", "Status"])

def load_students():
    if os.path.exists("students.csv"):
        return pd.read_csv("students.csv")
    else:
        return pd.DataFrame(columns=["Name", "Class", "Roll Number", "Contact"])

def load_staff():
    if os.path.exists("staff.csv"):
        return pd.read_csv("staff.csv")
    else:
        return pd.DataFrame(columns=["Name", "Position", "Contact", "Status"])

