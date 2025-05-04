from google import genai
from PIL import Image
from models import Report
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_report(image_path: str):
    # Construct the contents for the request
    contents = [
        "You are a Crop Assistant Agent. Your name is AgroPro who work for the company Attend Aura. Your job is to make a report about the crop disease."
    ]

    # Open the image and append it to the contents
    if image_path:
        try:
            img = Image.open(image_path)
            contents.append(img)
        except Exception as e:
            print(f"Error opening image: {e}")

    # Make the API call to generate the report
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=contents,
        config={
            'response_mime_type': 'application/json',
            'response_schema': Report,
        },
    )

    # Parse the response
    result = json.loads(response.text)
    return result

#Crop Name: Unknown

# Disease: Unknown

# Symptoms:
# Unknown
# Cause:
# Unknown
# Management:
# Unknown
# Prevention:
# Unknown
    