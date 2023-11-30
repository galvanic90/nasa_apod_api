import requests
import json
from fastapi import FastAPI

app = FastAPI()

url = 'https://api.nasa.gov/planetary/apod?api_key=0VdyL4qzq2P4OfTFJTV30pjKOOEj5HLjvf81QwBz'

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/apod-planetary")
async def planetary():
    raw_response = requests.get(url)
    json_response = raw_response.json()
    return json_response

# start_day:str, end_day
@app.get("/apod/count")
async def planetary():
    params = {'date':'2020-03-09'}
    raw_response = requests.get(url, params=params,)
    json_response = raw_response.json()
    return json_response