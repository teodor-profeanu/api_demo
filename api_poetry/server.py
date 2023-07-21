from pydantic import BaseModel

import api_poetry.service as ser
from fastapi import FastAPI
import uvicorn
import httpx

class TextItem(BaseModel):
    text: str


app = FastAPI()


@app.get("/hc")
def health_check():
    return {"status": "Healthy"}


@app.post("/words")
def words(item: TextItem):
    return {"words": ser.words(item.text)}


@app.post("/sentences")
def sentences(item: TextItem):
    return {"sentences": ser.sentences(item.text)}


@app.post("/paragraphs")
def paragraphs(item: TextItem):
    return {"paragraphs": ser.paragraphs(item.text)}


@app.post("/bigrams")
def bigrams(item: TextItem):
    return {"bigrams": ser.bigrams(item.text)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
