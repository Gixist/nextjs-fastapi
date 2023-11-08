from fastapi import FastAPI

app = FastAPI()

@app.get("/api/index")
def hello_world():
    return {"message": "Hello World"}