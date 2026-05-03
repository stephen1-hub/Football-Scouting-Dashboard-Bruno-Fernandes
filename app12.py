import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(layout="wide")

# -----------------------------
# IMAGE
# -----------------------------
image_path = "bruno.jpg"

def load_image(path):
    try:
        if os.path.exists(path):
            return Image.open(path)
        return None
    except:
        return None

image = load_image(image_path)

# -----------------------------
# HEADER
# -----------------------------
col1, col2 = st.columns([1, 3])

with col1:
    if image:
        st.image(image, width=180)
    else:
        st.warning("Image not found")

with col2:
    st.title("Bruno Fernandes")
    st.markdown("### Attacking Midfielder | Creative Playmaker")
    st.markdown("---")

# -----------------------------
# KPIs (FROM YOUR DATA)
# -----------------------------
total_goals = 7
total_xg = 11.38
total_xa = 15.75

col1, col2, col3, col4 = st.columns(4)

col1.metric("Goals", total_goals, round(total_goals - total_xg, 2))
col2.metric("xG", total_xg)
col3.metric("xA", total_xa)
col4.metric("xA/90", "Elite", "Creator")

st.markdown("---")

# -----------------------------
# ATTRIBUTES (SCOUT PROFILE)
# -----------------------------
st.markdown("### Player Attributes")

attributes = {
    "Creativity": 95,
    "Vision": 94,
    "Passing Range": 92,
    "Decision Making": 78,
    "Finishing": 70,
    "Ball Striking": 75
}

for attr, value in attributes.items():
    st.markdown(f"**{attr}**")
    st.progress(value / 100)

st.markdown("---")

# -----------------------------
# DATA (YOUR REAL STRUCTURE)
# -----------------------------
zone_df = pd.DataFrame({
    "zone": ["Out of box", "Penalty area", "Six-yard box"],
    "shots": [40, 34, 3],
    "goals": [1, 6, 1],
    "xG": [1.52, 8.34, 1.52]
})

type_df = pd.DataFrame({
    "type": ["Right foot", "Left foot", "Head"],
    "shots": [66, 9, 2],
    "goals": [8, 0, 0],
    "xG": [10.00, 1.07, 0.32]
})

situation_df = pd.DataFrame({
    "situation": ["Open play", "Penalty", "Direct FK", "Corner"],
    "shots": [57, 6, 5, 5],
    "goals": [3, 4, 1, 0],
    "xG": [6.04, 4.57, 0.44, 0.16]
})

position_df = pd.DataFrame({
    "position": ["MC", "AMC"],
    "xG90": [0.47, 0.25],
    "xA90": [0.32, 0.72]
})

# -----------------------------
# SIDEBAR
# -----------------------------
section = st.sidebar.radio("Navigate", [
    "Overview",
    "Shot Zones",
    "Shot Types",
    "Situations",
    "Role Analysis",
    "Scouting Summary"
])

# -----------------------------
# OVERVIEW
# -----------------------------
if section == "Overview":

    st.header("Performance Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Goals", total_goals)
    col2.metric("xG", total_xg)
    col3.metric("Shots", zone_df["shots"].sum())

    fig, ax = plt.subplots()
    ax.bar(["Goals", "xG"], [total_goals, total_xg])
    ax.set_title("Goals vs xG")
    st.pyplot(fig)

# -----------------------------
# SHOT ZONES
# -----------------------------
elif section == "Shot Zones":

    st.header("Shot Zone Analysis")

    fig, ax = plt.subplots()
    ax.bar(zone_df["zone"], zone_df["shots"])
    ax.set_title("Shot Distribution")
    plt.xticks(rotation=20)
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    ax2.bar(zone_df["zone"], zone_df["xG"])
    ax2.set_title("xG by Zone")
    plt.xticks(rotation=20)
    st.pyplot(fig2)

    st.dataframe(zone_df)

# -----------------------------
# SHOT TYPES
# -----------------------------
elif section == "Shot Types":

    st.header("Shot Type Breakdown")

    fig, ax = plt.subplots()
    ax.bar(type_df["type"], type_df["shots"])
    ax.set_title("Shots by Type")
    plt.xticks(rotation=20)
    st.pyplot(fig)

    st.dataframe(type_df)

# -----------------------------
# SITUATIONS
# -----------------------------
elif section == "Situations":

    st.header("Situation Analysis")

    fig, ax = plt.subplots()
    ax.pie(situation_df["shots"], labels=situation_df["situation"], autopct="%1.1f%%")
    st.pyplot(fig)

    st.dataframe(situation_df)

# -----------------------------
# ROLE ANALYSIS (NEW + IMPORTANT)
# -----------------------------
elif section == "Role Analysis":

    st.header("Role-Based Output")

    fig, ax = plt.subplots()
    ax.bar(position_df["position"], position_df["xA90"])
    ax.set_title("xA/90 by Role")
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    ax2.bar(position_df["position"], position_df["xG90"])
    ax2.set_title("xG/90 by Role")
    st.pyplot(fig2)

    st.dataframe(position_df)

# -----------------------------
# SCOUTING SUMMARY
# -----------------------------
elif section == "Scouting Summary":

    st.header("Scouting Report")

    st.markdown("""
    ### Player Profile
    - High-risk creative midfielder  
    - Elite chance creator  
    - Role-dependent attacking output  

    ### Strengths
    - Exceptional vision and chance creation (xA)  
    - Strong influence in advanced midfield roles  
    - High involvement in attacking build-up  

    ### Weaknesses
    - Inefficient long-range shot selection  
    - Over-reliance on outside-box attempts  
    - Limited presence in six-yard box  

    ### Tactical Insight
    - Creativity peaks when deployed as an attacking midfielder (AMC)  
    - Deeper roles increase goal threat but reduce playmaking output  
    - Significant attacking contribution from set-piece situations  

    ### Analyst Verdict
    > Elite creative hub with high-risk decision making.  
    > Best utilized in systems that maximise attacking freedom  
    > and reduce reliance on his shot efficiency.
    """)