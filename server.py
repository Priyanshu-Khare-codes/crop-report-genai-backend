from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from aiservice import generate_report
from models import Report
import tempfile
import os

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def status():
    return {"status": "Server is running"}

@app.post("/report", response_model=Report)
async def report(image: UploadFile = File(...)):
    try:
        if image:
            # Create temporary file to save the uploaded image
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(image.filename)[1]) as temp_file:
                temp_file.write(await image.read())
                image_path = temp_file.name

        # Process the image and generate a report
        result = generate_report(image_path)

        # Clean up the temporary file
        os.remove(image_path)

        return result
    
    except Exception as e:
        return {"error": str(e)}