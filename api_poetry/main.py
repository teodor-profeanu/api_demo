from collections import Counter

from fastapi import FastAPI
import uvicorn
import string
import re
from pydantic import BaseModel


class TextItem(BaseModel):
    text: str


def remove_punctuation(text):
    translator = str.maketrans(string.punctuation, " " * len(string.punctuation))
    return text.translate(translator)


app = FastAPI()


@app.get("/hc")
def health_check():
    return {"status": "Healthy"}


@app.post("/words")
def words_func(item: TextItem):
    return {"words": remove_punctuation(item.text).split()}


@app.post("/sentences")
def sentences(item: TextItem):
    return {"sentences": [x.strip() for x in re.split(r'[.!?]', item.text) if len(x.strip()) > 0]}


@app.post("/paragraphs")
def paragraphs(item: TextItem):
    return {"paragraphs": [x for x in item.text.split('\n') if len(x.strip()) > 0]}


@app.post("/bigrams")
def bigrams(item: TextItem):
    words = remove_punctuation(item.text).lower().split()
    pairs = [' '.join([words[i], words[i+1]]) for i in range(0, len(words)-1)]
    counter = Counter(pairs).most_common()
    max_size = 5 if len(counter) > 5 else len(counter)
    return {"bigrams": {counter[i][0]:counter[i][1] for i in range(0, max_size)}}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
