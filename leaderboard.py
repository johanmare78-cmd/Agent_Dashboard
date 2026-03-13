import streamlit as st
import pandas as pd


def show_leaderboard(df):

    # ---------- CLEAN DATA ----------
    df.columns = df.columns.str.strip()
    df = df.fillna(0)

    numeric_cols = [
        "Weekly Target",
        "Weekly Done",
        "Monitor On",
        "Monitor Target",
        "Monitor Need",
        "Commission Target",
        "Commission On",
        "Commission Need"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # ---------- TITLE ----------
    st.markdown(
        "<h1 style='text-align:center;'>📺 AGENT PERFORMANCE WALLBOARD</h1>",
        unsafe_allow_html=True
    )

    # ---------- TEAM TOTALS ----------
    weekly_done = df["Weekly Done"].sum()
    weekly_target = df["Weekly Target"].sum()

    monitor_done = df["Monitor On"].sum()
    monitor_target = df["Monitor Target"].sum()

    weekly_progress = weekly_done / weekly_target if weekly_target else 0
    monitor_progress = monitor_done / monitor_target if monitor_target else 0

    weekly_percent = int(weekly_progress * 100)
    monitor_percent = int(monitor_progress * 100)

    # ---------- MONITOR BAR ----------
    st.markdown(
        f"""
<div style="margin-bottom:25px;">

<div style="font-size:24px;font-weight:700;">
📊 TEAM MONITOR TARGET
</div>

<div style="background:#e5e7eb;border-radius:20px;height:26px;overflow:hidden;margin-top:8px;">

<div style="
width:{monitor_percent}%;
height:26px;
background:linear-gradient(90deg,#22c55e,#4ade80);
">
</div>

</div>

<div style="
margin-top:10px;
font-size:22px;
font-weight:900;
color:#111827;
">
{monitor_percent}% Completed
</div>

<div style="
font-size:20px;
font-weight:700;
background:#f3f4f6;
padding:6px 12px;
border-radius:8px;
display:inline-block;
margin-top:4px;
">
R{int(monitor_done):,} / R{int(monitor_target):,}
</div>

</div>
""",
        unsafe_allow_html=True
    )

    # ---------- WEEKLY SALES ----------
    st.markdown(
        f"""
<div style="margin-bottom:35px;">

<div style="font-size:24px;font-weight:700;">
💰 TEAM WEEKLY SALES
</div>

<div style="background:#e5e7eb;border-radius:20px;height:26px;overflow:hidden;margin-top:8px;">

<div style="
width:{weekly_percent}%;
height:26px;
background:linear-gradient(90deg,#22c55e,#4ade80);
">
</div>

</div>

<div style="
margin-top:10px;
font-size:22px;
font-weight:900;
color:#111827;
">
{weekly_percent}% Completed
</div>

<div style="
font-size:20px;
font-weight:700;
background:#f3f4f6;
padding:6px 12px;
border-radius:8px;
display:inline-block;
margin-top:4px;
">
R{int(weekly_done):,} / R{int(weekly_target):,}
</div>

</div>
""",
        unsafe_allow_html=True
    )

    # ---------- CALCULATIONS ----------
    df["Weekly Need"] = df["Weekly Target"] - df["Weekly Done"]

    # ---------- AGENT OF THE WEEK ----------
    top_agent = df.loc[df["Weekly Done"].idxmax()]

    if "confetti_shown" not in st.session_state:
        st.balloons()
        st.session_state.confetti_shown = True

    st.markdown(
        f"""
<div style="
background:linear-gradient(90deg,#facc15,#fde047);
padding:25px;
border-radius:16px;
text-align:center;
font-size:30px;
font-weight:900;
margin-bottom:40px;
box-shadow:0 0 25px rgba(250,204,21,0.8);
">

🏆 AGENT OF THE WEEK 🏆

<div style="font-size:34px;margin-top:8px;">
{top_agent['Agent Name']}
</div>

<div style="font-size:26px;margin-top:6px;">
💰 R{int(top_agent['Weekly Done']):,}
</div>

</div>
""",
        unsafe_allow_html=True
    )

    # ---------- AGENT CARDS ----------
    agents = df.to_dict("records")

    cards_per_row = 4

    for i in range(0, len(agents), cards_per_row):

        cols = st.columns(len(agents[i:i + cards_per_row]))

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
🎯 Target: R{int(agent['Monitor Target']):,}<br>
💰 On: R{int(agent['Monitor On']):,}<br>
👀 Need: R{int(agent['Monitor Need']):,}
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