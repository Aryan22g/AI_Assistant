from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles  import StaticFiles
from fastapi.responses import FileResponse

# create webapp, to handle errors, to build form for fastAPI (request submissions)
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
MODEL_NAME = "qwq" # change to "llama3" if preferred

@app.get("/")
def serve_homepage():
    """ Serve the index.html file when accessing the root URL """
    return FileResponse(os.path.join("static","index.html"))

@app.post("/chat")
def chat_with_ai(user_query: str = Form(...)):
    headers = {"Content-Type": "application/json"}
    # create a structured prompt for customer support chatbot
    prompt=f"""You are a customer support chatbot. Answer the user's question professionaly and concisely.
    User: {user_query}
    Chatbot:"""
    
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
        chatbot_response = json_response.get("response", "I'm sorry, but I couldn't generate a response.")
        
        return {"response": chatbot_response}
    
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
