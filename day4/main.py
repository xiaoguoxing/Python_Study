from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def ai():
    return {"message":"Hello World"}