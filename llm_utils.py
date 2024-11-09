from transformers import pipeline

# Initialize language model
nlp = pipeline("text-generation", model="gpt-3.5-turbo")

def generate_itinerary(city, interests, start_time, end_time):
    prompt = f"Plan a one-day itinerary in {city} from {start_time} to {end_time} for someone interested in {', '.join(interests)}."
    result = nlp(prompt, max_length=200)
    itinerary = result[0]["generated_text"]
    return itinerary
