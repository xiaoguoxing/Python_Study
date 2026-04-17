from fastapi import FastAPI
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")
app = FastAPI()

@app.get("/ask")
def ask(q:str):
    res = client.chat.completions.create(
        model="gpt-5.4",
        messages=[
            {"role":'user',"content":q}
        ],
    )
    return {"message":res.choices[0].message.content}