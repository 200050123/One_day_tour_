from pydantic import BaseModel
from typing import List

class UserPreferences(BaseModel):
    user_id: str
    city: str
    start_time: str
    end_time: str
    budget: int
    interests: List[str]

class ItineraryItem(BaseModel):
    name: str
    start_time: str
    end_time: str
    transportation: str
    cost: float
    distance: str

class ItineraryResponse(BaseModel):
    itinerary: List[ItineraryItem]
