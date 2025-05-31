Step 1: Project Setup
    a. check ollama installation
    b. install mistral 7B:-       ollama pull mistral
    c. pip install fastapi uvicorn requests
Step 2: Create the Backend with FastAPI
Step 3: Build the web UI
Step 4: Run and test your AI summariser
    a. Steps To run 
        i. on Terminal:      uvicorn app:app --host 0.0.0.0 --port 8000 --reload
        ii. On Browser:       http://0.0.0.0:8000
