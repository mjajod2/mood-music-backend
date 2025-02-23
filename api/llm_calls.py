from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=api_key)

print(os.environ.get('GEMINI_API_KEY'))
def send_genre_request_to_llm(query_text):
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=f"what type of music genre fits the following mood description: {query_text}? Only tell me genre name")  # need to pass the query sentence here instead of the hardcoded one
    return response.text

def send_artist_recommendation_request_to_llm(query_text):
    request = client.models.generate_content(
    model="gemini-2.0-flash", contents=f"which artist would you recommend listening to if the user says this: {query_text}? just give one artist name.")
    return request.text
    
def send_request_for_language(query_text, language):
    request = client.models.generate_content(
    model="gemini-2.0-flash", contents=f"which artist would you recommend listening to if the user says this: {query_text}? Only tell me artist name? tell me the recommendation for artist whose songs are in {language} language")
    return request.text
