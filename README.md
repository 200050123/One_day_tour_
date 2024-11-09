Project Structure Overview
Backend:

Implement APIs with FastAPI for different services (user data handling, itinerary generation, memory storage).
Implement agents using LLMs and integrate them with each part of the itinerary planning.
Frontend:

Use Streamlit to create a chat-based interface where the user can input preferences and view updates to their itinerary.
Database:

Use Neo4j for graph-based memory storage to save and retrieve user preferences across sessions.

The application will be a chat-based system to help users plan a one-day tour in any city. The key features involve:


├── backend
│   ├── main.py               # FastAPI app with endpoints
│   ├── database.py           # Neo4j connection setup
│   ├── models.py             # Pydantic models
│   ├── llm_utils.py          # Functions for LLM processing
│   └── itinerary_utils.py    # Itinerary generation and optimization
├── frontend
│   └── app.py                # Streamlit interface


# Run the Application

uvicorn backend.main:app --reload
streamlit run frontend/app.py
# One_day_tour
