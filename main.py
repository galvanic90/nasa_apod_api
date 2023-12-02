import requests
import json
import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

url = 'https://api.nasa.gov/planetary/apod?api_key=0VdyL4qzq2P4OfTFJTV30pjKOOEj5HLjvf81QwBz'

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/apod-today")
async def get_today_apod():
    raw_response = requests.get(url)
    json_response = raw_response.json()
    return json_response

# start_day:str, end_day
@app.get("/apod/date")
async def search_by_date(day: datetime.date):
    params = {'date':day}
    raw_response = requests.get(url, params=params)
    json_response = raw_response.json()
    return json_response

@app.get("/apod/pic-group")
async def get_a_set_of_APOD(number: int):
    params = {'count':number}
    raw_response = requests.get(url, params=params)
    json_response = raw_response.json()
    return json_response