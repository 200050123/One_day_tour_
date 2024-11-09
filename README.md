.
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
