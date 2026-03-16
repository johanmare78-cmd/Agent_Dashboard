import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh

from config import REFRESH_INTERVAL
from utils.calculations import calculate_stats
from dashboard.leaderboard import show_leaderboard


st.set_page_config(page_title="Agent Stats", layout="wide")

# Auto refresh
st_autorefresh(interval=REFRESH_INTERVAL)

# Clear cache so Excel reloads
st.cache_data.clear()

try:

    # Load Excel directly
    df = pd.read_excel("Agent_Dashboard.xlsx")

    # Run calculations
    df = calculate_stats(df)

    # Show dashboard
    show_leaderboard(df)

except Exception as e:

    st.error(f"Error loading data: {e}")