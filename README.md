# Python PDF Processor via Gemini API

Small experimental application that leverages Google Gemini's API services to process fictional "Warehouse Inventory" PDF files, outputting their information into JSON files.

Utilizes Python + FastAPI to provide end-points that interact with the API.

Run the **fastapi dev main.py** command to start.

## Current endpoints

- **"/"** - Processes the original warehouse inventory PDF file and returns a JSON with the appropriate data from the file.
- **"/generateDoc"** - Utilizes the original warehouse inventory PDF file to generate a new, original list of items, quantities and manufacturers.
