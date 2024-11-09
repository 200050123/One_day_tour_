import streamlit as st
import requests

st.title("One-Day Tour Planning Assistant")

# Input fields
user_id = st.text_input("User ID")
city = st.text_input("City to visit")
start_time = st.time_input("Start Time")
end_time = st.time_input("End Time")
budget = st.number_input("Budget", min_value=0)
interests = st.multiselect("Interests", ["Culture", "Adventure", "Food", "Shopping"])

# Submit Preferences
if st.button("Submit Preferences"):
    preferences = {
        "user_id": user_id,
        "city": city,
        "start_time": start_time.strftime('%H:%M'),
        "end_time": end_time.strftime('%H:%M'),
        "budget": budget,
        "interests": interests
    }
    response = requests.post("http://localhost:8000/preferences", json=preferences)
    st.write(response.json())

# Generate Itinerary
if st.button("Generate Itinerary"):
    response = requests.get(f"http://localhost:8000/generate_itinerary?user_id={user_id}")
    if response.status_code == 200:
        st.write("Generated Itinerary:")
        for item in response.json()["itinerary"]:
            st.write(item)
    else:
        st.error("Could not generate itinerary.")
