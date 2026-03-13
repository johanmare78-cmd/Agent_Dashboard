import streamlit as st
from streamlit_autorefresh import st_autorefresh

from config import REFRESH_INTERVAL
from data.excel_loader import load_excel_data
from utils.calculations import calculate_stats
from dashboard.leaderboard import show_leaderboard


st.set_page_config(page_title="Agent Stats", layout="wide")

# Auto refresh every few seconds
st_autorefresh(interval=REFRESH_INTERVAL)

# Clear cache so Excel reloads
st.cache_data.clear()

try:

    df = load_excel_data()

    df = calculate_stats(df)

    show_leaderboard(df)

except Exception as e:

    st.error(f"Error loading data: {e}")