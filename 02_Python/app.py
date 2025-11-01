import streamlit as st
import pickle
import pandas as pd


with open("game_model.pkl", "rb") as f:
    model = pickle.load(f)


st.title("🎮 Game Category Predictor")

st.markdown("Enter the game details to predict its category:")

# User input
target_audience = st.selectbox("Target Audience", ["Teens", "Adults", "Teens/Adults"])
age_range = st.selectbox("Age Range", ["13-19", "13-25", "20-40"])
skills = st.selectbox("Skills", ["Low", "Medium", "High"])
multiplayer = st.selectbox("Multiplayer", ["Yes", "No"])
publisher = st.selectbox("Publisher", ["Electronic Arts", "Ubisoft", "Konami", "Warner Bros.", "Other"])
name_categorized = st.text_input("Game Name")
publisher_category = st.selectbox("Publisher Category", ["EA", "Ubisoft", "Konami", "Warner Bros", "Other"])
platform = st.selectbox("Platform", ["PS2", "PS3", "X360", "XOne", "DS", "PS"])

# Collect inputs into a dataframe
input_df = pd.DataFrame({
    "Target_Audience": [target_audience],
    "Age_Range": [age_range],
    "Skills": [skills],
    "Multiplayer": [multiplayer],
    "Publisher": [publisher],
    "Name_Categorized": [name_categorized],
    "Publisher_Category": [publisher_category],
    "Platform": [platform]
})

# Predict button
if st.button("Predict Category"):
    pred = model.predict(input_df)
    st.success(f"Predicted Category: {pred[0]}")
