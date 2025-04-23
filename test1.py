from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Used when file is larger than 20 MB
# img = client.files.upload(file="media/tomato.jpg")

# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents=[img, "Identify the Crop"]
# )

# Used when file is less than 20 MB
with open("media/tomato.jpg", "rb") as f:
    img = f.read()

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        types.Part.from_bytes(
            data=img,
            mime_type='image/jpeg',
        ),
        "Identify the Crop"
    ]
)

print("Response:\n", response.text)