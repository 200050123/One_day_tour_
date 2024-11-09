from fastapi import FastAPI, HTTPException
from models import UserPreferences, ItineraryResponse
from database import store_user_preferences, get_user_preferences
from itinerary import generate_itinerary
import uvicorn

app = FastAPI()

@app.post("/preferences", status_code=201)
async def create_preferences(preferences: UserPreferences):
    store_user_preferences(preferences.dict())
    return {"message": "Preferences stored successfully"}

@app.get("/preferences/{user_id}", response_model=UserPreferences)
async def read_preferences(user_id: str):
    preferences = get_user_preferences(user_id)
    if not preferences:
        raise HTTPException(status_code=404, detail="User preferences not found")
    return preferences

@app.get("/generate_itinerary", response_model=ItineraryResponse)
async def generate_itinerary_route(user_id: str):
    preferences = get_user_preferences(user_id)
    if not preferences:
        raise HTTPException(status_code=404, detail="User preferences not found")
    
    itinerary_text = generate_itinerary(preferences['city'], preferences['interests'], preferences['start_time'], preferences['end_time'])
    # Parse itinerary_text to ItineraryResponse format (skipping detailed parsing for simplicity)
    itinerary = [{"name": place, "start_time": "09:00", "end_time": "10:00", "transportation": "walk", "cost": 0, "distance": "1 km"} for place in itinerary_text.split('\n')]
    return {"itinerary": itinerary}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
