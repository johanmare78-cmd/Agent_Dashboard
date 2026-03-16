import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# Page setup
st.set_page_config(page_title="Agent Stats Dashboard", layout="wide")

# Auto refresh every 15 seconds
st_autorefresh(interval=15000)

# OneDrive Excel link (direct download)
excel_url = "https://1drv.ms/x/c/12682cf798395550/IQAAUmahz2yiSKQ9IpOs8sx_AXYbZCRX0mOmM3yrKgVDEhg?download=1"


def calculate_stats(df):

    df["Weekly Need"] = df["Weekly Target"] - df["Weekly Done"]
    df["Monitor Need"] = df["Monitor Target"] - df["Monitor On"]
    df["Commission Need"] = df["Commission Target"] - df["Commission On"]

    return df


def show_dashboard(df):

    st.title("📺 Agent Performance Dashboard")

    df = df.fillna(0)

    agents = df.to_dict("records")

    cards_per_row = 4

    for i in range(0, len(agents), cards_per_row):

        cols = st.columns(cards_per_row)

        for col, agent in zip(cols, agents[i:i + cards_per_row]):

            with col:

                st.markdown(
                    f"""
<div style="
padding:20px;
border-radius:14px;
text-align:center;
margin-bottom:25px;
box-shadow:0 0 10px rgba(0,0,0,0.2);
background:white;
">

<div style="font-size:22px;font-weight:900;margin-bottom:12px;">
👤 {agent['Agent Name']}
</div>

<div style="background:#1f2937;color:white;padding:10px;border-radius:8px;margin-bottom:8px;">
<b>WEEKLY</b><br>
🎯 Target: R{int(agent['Weekly Target']):,}<br>
💰 On: R{int(agent['Weekly Done']):,}<br>
👀 Need: R{int(agent['Weekly Need']):,}
</div>

<div style="background:#1f2937;color:white;padding:10px;border-radius:8px;margin-bottom:8px;">
<b>MONITOR</b><br>
🎯 Target: {int(agent['Monitor Target'])}<br>
💰 On: {int(agent['Monitor On'])}<br>
👀 Need: {int(agent['Monitor Need'])}
</div>

<div style="background:#1f2937;color:white;padding:10px;border-radius:8px;margin-bottom:10px;">
<b>COMMISSION</b><br>
🎯 Target: R{int(agent['Commission Target']):,}<br>
💰 On: R{int(agent['Commission On']):,}<br>
👀 Need: R{int(agent['Commission Need']):,}
</div>

</div>
""",
                    unsafe_allow_html=True
                )


try:

    # Load Excel from OneDrive
    df = pd.read_excel(excel_url)

    df = calculate_stats(df)

    show_dashboard(df)

except Exception as e:

    st.error(f"Error loading data: {e}")
