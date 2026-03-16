import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from dashboard.leaderboard import show_leaderboard

REFRESH_INTERVAL = 15000

st.set_page_config(page_title="Agent Stats", layout="wide")

# Auto refresh
st_autorefresh(interval=REFRESH_INTERVAL)

def calculate_stats(df):

    df["Weekly Need"] = df["Weekly Target"] - df["Weekly Done"]
    df["Monitor Need"] = df["Monitor Target"] - df["Monitor On"]
    df["Commission Need"] = df["Commission Target"] - df["Commission On"]

    return df

try:

    df = pd.read_excel("Agent_Dashboard.xlsx")

    df = calculate_stats(df)

    show_leaderboard(df)

except Exception as e:

    st.error(f"Error loading data: {e}")
