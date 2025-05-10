import httpx
import requests
from fastapi import FastAPI
from geopy.geocoders import Nominatim

loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode()
print(getLoc)
app = FastAPI()

@app.get("/")
def root():
  return {"message": "Hello world! You have reached the root."}

@app.get("/get-sea-level")
def info():
  url = "https://marine-api.open-meteo.com/v1/marine?latitude=54.544587&longitude=10.227487&hourly=sea_level_height_msl"
  info = requests.get(url).json()
  return {"info": info}