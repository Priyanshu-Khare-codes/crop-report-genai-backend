# 🌾 Agro Pro

Agro Pro is an intelligent crop disease detection system that helps farmers and agriculturists identify crop diseases and get effective cures. Our goal is to improve crop health and boost agricultural productivity using cutting-edge AI.

🚀 Features

- 🌱 Detects crop diseases from images
- 💊 Suggests accurate and relevant cures
- ⚡ FastAPI backend for blazing-fast API performance
- 🤖 Integrated with Gemini for intelligent response generation

🛠️ Technologies Used

- **FastAPI** – High-performance web framework for Python
- **Gemini** – Used for generating natural-language treatment recommendations
- **Python**

📦 Installation

1. Clone the repository:
   ```bash
   https://github.com/Priyanshu-Khare-codes/crop-report-genai-backend
   cd crop-report-genai-backend
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Set up your .env file: Create a .env file in the root directory with your Google API key:
   ```bash
   GOOGLE_API_KEY=YOUR_API_KEY
   ```

4. Run the server:
   ```bash
   uvicorn server:app --reload
   ```

📷 Usage
Upload an image of the affected crop.

The app analyzes the image using a trained model.

Gemini generates a detailed cure and advice based on the detected of the disease of the crop and the plants.


