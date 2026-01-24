from fastapi import FastAPI
import pathlib
from typing import Optional
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json

app = FastAPI()
BASE_DIR = pathlib.Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR.parent / "models"
SMS_SPAM_MODEL_PATH = MODEL_DIR / "spam-sms"
MODEL_PATH = SMS_SPAM_MODEL_PATH / "spam-model.h5"
TOKENIZER_PATH = SMS_SPAM_MODEL_PATH / "spam-classifer-tokenizer.json"
METADATA_PATH = SMS_SPAM_MODEL_PATH / "spam-classifer-metadata.json"

AI_MODEL = None
AI_TOKENIZER = None
MODEL_METADATA = {}
labels_legend_inverted = {}


@app.on_event("startup")
def on_startup():
    global AI_MODEL,AI_TOKENIZER,MODEL_METADATA,labels_legend_inverted
    # load my model
    if MODEL_PATH.exists():
      AI_MODEL = load_model(MODEL_PATH)
    if TOKENIZER_PATH.exists():
      t_json = TOKENIZER_PATH.read_text()
      AI_TOKENIZER = tokenizer_from_json(t_json)   
      print(AI_TOKENIZER) 
    if METADATA_PATH.exists():
       MODEL_METADATA = json.loads(METADATA_PATH.read_text())
       labels_legend_inverted = MODEL_METADATA['labels_legend_inverted']

def predict(query:str):
   # sequences
   # pad_sequences
   # model.predict
   # convert to labels
   sequences = AI_TOKENIZER.texts_to_sequences([query])
   maxlen = MODEL_METADATA.get('max_sequence') or 280
   x_input = pad_sequences(sequences, maxlen=maxlen)
   print(x_input)
   print(x_input.shape)
   preds_array = AI_MODEL.predict(x_input) # list of predict
   preds = preds_array[0]
   print('PRED: ',preds)
   return {}
   

@app.get("/")
def read_index(q:Optional[str]=None):
    global AI_MODEL,MODEL_METADATA,labels_legend_inverted
    query = q or "hello world"
    predict(query)
    return {"query": query, **MODEL_METADATA, "legend-":labels_legend_inverted}