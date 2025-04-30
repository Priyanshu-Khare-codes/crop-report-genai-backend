from google import genai
from google.genai import types
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

img = Image.open("media/tomato.jpg")
response = client.models.generate_content(
    model="gemini-2.0-flash-lite",
    config = types.GenerateContentConfig(
        system_instruction="You are a Crop Assistant Agent. Your name is AgroPro who work for the company Attend Aura."
    ),
    contents=[img, "Identify the crop"]
)
print(response.text)