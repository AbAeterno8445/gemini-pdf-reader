import os
from google import genai
from fastapi import FastAPI

app = FastAPI()

aiClient = genai.Client(api_key=os.getenv('GEMINI_TEST_API_KEY'))


@app.get("/")
async def root():
    aiResponse = aiClient.models.generate_content(
        model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
    )
    return {"message": aiResponse.text}