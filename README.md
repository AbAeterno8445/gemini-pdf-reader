# Python PDF Processor via Gemini API

Small experimental application that leverages Google Gemini's API services to process fictional "Warehouse Inventory" PDF files, outputting their information into JSON files.

Utilizes Python + FastAPI to provide end-points that interact with the API, and Pydantic for schema data validation.

Run the **fastapi dev main.py** command to start.

## Current endpoints

- **/extractPDF** (POST) - Processes the original warehouse inventory PDF file and returns a JSON with the appropriate data from the file. Receives the PDF file in a **fileUpload** field.
- **/getPrompt** (GET) - Returns the prompt that is sent to the Gemini API.
