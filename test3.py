from google import genai
from PIL import Image
from models1 import Report
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

img = Image.open("media/pogo.jpg")
response = client.models.generate_content(
    model="gemini-1.5-pro",
    contents=[img, "You are a Crop Assistant Agent. Your name is AgroPro who work for the company Attend Aura. Your job is to make a report about the crop disease."],
    config={
        'response_mime_type': 'application/json',
        'response_schema': Report,
    },
)
result = json.loads(response.text)

def printReport():
    print("Crop Name: ", result['crop_name'])
    print("Crop Disease: ", result['crop_disease'])
    print("Crop Disease Symptoms: ")
    for idx, item in enumerate(result['crop_disease_symptoms']):
        print(f"{idx+1}: {item}")
    print("Crop Disease Cause: ")
    for idx, item in enumerate(result['crop_disease_cause']):
        print(f"{idx+1}: {item}")
    print("Crop Disease Management: ")
    for idx, item in enumerate(result['crop_disease_management']):
        print(f"{idx+1}: {item}")
    print("Crop Disease Prevention: ")
    for idx, item in enumerate(result['crop_disease_prevention']):
        print(f"{idx+1}: {item}")

printReport()
