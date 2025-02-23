from google import genai

client = genai.Client(api_key="AIzaSyAFFGggwcKwa_9ABXTMZTaAWgIn4A5Nm6c")

def send_request_to_llm(query_text):
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents="what type of music genre fits the following mood description: `I am feeling sad and nostalgic`? Only tell me genre name")  # need to pass the query sentence here instead of the hardcoded one
    print(response.text)