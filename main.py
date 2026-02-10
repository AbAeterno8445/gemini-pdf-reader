from google import genai
from google.genai import types
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
import os
import pathlib

# Pydantic schema definitions
class InventoryItem(BaseModel):
    ID: str = Field(description="Numeric ID of the item, in 3 digits.")
    name: str = Field(description="Name of the item.")
    category: str = Field(description="Category group of the item.")
    quantity: int = Field(description="Remaining amount of this item as per the inventory.")
    manufacturer: str = Field(description="Company that manufactured the item.")
    status: str = Field(description="Stock status for the item.")

class InventoryOutput(BaseModel):
    date: str = Field(description="The date the inventory was made in.")
    notes: str = Field(description="Additional notes about this inventory, if necessary.")
    items: List[InventoryItem]

# FastAPI app
app = FastAPI()

# Google genai client
aiClient = genai.Client(api_key=os.getenv('GEMINI_TEST_API_KEY'))

# PDF file
pdfPath = pathlib.Path("input/Warehouse Banana Test.pdf")

@app.get("/")
async def root():
    prompt = ("Read the given PDF document, and extract its items' fields into the appropriate schema. "
              "The inventory date corresponds to the date at the top of the document. "
              "Use the 'notes' field to append any outstanding status about this inventory, in a few words.")
    aiResponse = aiClient.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
            types.Part.from_bytes(
                data=pdfPath.read_bytes(),
                mime_type='application/pdf'
            ),
            prompt
        ],
        config={
            "response_mime_type": "application/json",
            "response_json_schema": InventoryOutput.model_json_schema()
        }
    )
    newInventory = InventoryOutput.model_validate_json(aiResponse.text)
    return newInventory

@app.get("/generateDoc")
async def generateDocRoute():
    prompt = "Given this PDF document, generate a list of items of a similar nature (fruits, vegetables), making up new quantities and manufacturers, and the approriate stock status (which can only be one of the three present). Date can be anything before 2026."
    aiResponse = aiClient.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
            types.Part.from_bytes(
                data=pdfPath.read_bytes(),
                mime_type='application/pdf'
            ),
            prompt
        ],
        config={
            "response_mime_type": "application/json",
            "response_json_schema": InventoryOutput.model_json_schema()
        }
    )
    newList = InventoryOutput.model_validate_json(aiResponse.text)
    return newList

@app.get("/test")
async def testRoute():
    return {"message": "Test route operational."}