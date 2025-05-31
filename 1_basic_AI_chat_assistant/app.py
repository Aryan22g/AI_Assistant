from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles  import StaticFiles
from fastapi.responses import FileResponse

# create webapp, to handle errors, to define query params for api endpoint
# service static files from a directory
# to return index.html when response comes

import requests
import os
import json

app = FastAPI()

# serve frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")

#ollam settings
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral" # change to "llama3" if preferred

@app.get("/")
def serve_homepage():
    """ Serve the index.html file when accessing the root URL """
    return FileResponse(os.path.join("static","index.html"))

@app.post("/chat")
def chat(prompt: str = Query(..., description="User prompt for AI model")):
    headers = {"Content-Type": "application/json"}
    
    try:
        #send requests to ollama
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False},
            headers=headers
        )

        #log the response for debugging
        print("Ollama Response:", response.text)
        
        # ensure valid json response
        response_data = response.text.strip()
        try:
            json_response = json.loads(response_data)
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail=f"Invalid JSON response from Ollama: {response_data}")
        
        # extract ai response
        ai_response = json_response.get("response")
        if not ai_response:
            raise HTTPException(status_code=500, detail=f"No valid response received from Ollama")
        
        return {"response": ai_response}
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Request to ollama failed: {str(e)}")
    
# Run the API server
if __name__ == "__main__":
    import uvicorn
    #starts api server on mentioned host and port and auto reloads on port changes
    uvicorn.run(app, host="0.0.0.0",port=8000, reload=True)
    
# Steps To run 
# on Terminal:      uvicorn app:app --host 0.0.0.0 --port 8000 --reload
# On Browser:       http://0.0.0.0:8000
