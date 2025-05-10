import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
  return {"message": "Hello world! You have reached the root."}

@app.get("/get-sea-level")
def seaLevel():
  url = "https://marine-api.open-meteo.com/v1/marine?latitude=34.052235&longitude=124.5085&hourly=sea_level_height_msl"
  info = requests.get(url).json()

  # Extract and zip the data
  times = info["hourly"]["time"]
  sea_levels = info["hourly"]["sea_level_height_msl"]

  sea_level_data = [
      {"datetime": t, "sea_level_height_msl": s}
      for t, s in zip(times, sea_levels)
  ]

  return {"info": sea_level_data}

@app.get("/get-sea-temp")
def seaTemp():
  url = "https://marine-api.open-meteo.com/v1/marine?latitude=34.052235&longitude=124.5085&hourly=sea_surface_temperature"

  temp = requests.get(url).json()

  return {"sea temp": temp}

@app.get("/get-sea-current")
def seaCurrentVelocity():
  url = "https://marine-api.open-meteo.com/v1/marine?latitude=34.052235&longitude=124.5085&hourly=ocean_current_velocity"
  info = requests.get(url).json()
  times = info["hourly"]["time"]
  ocean_curent_velocity = info["hourly"]["ocean_current_velocity"]

  ocean_curent_velocity = [
      {"datetime": t, "ocean_current_velocity": s}
      for t, s in zip(times, ocean_curent_velocity)
  ]

  return {"sea current velocity": ocean_curent_velocity}

@app.get("/get-sea-wave-height")
def seaWaveHeight():
  url = "https://marine-api.open-meteo.com/v1/marine?latitude=34.052235&longitude=124.5085&hourly=wave_height"
  info = requests.get(url).json()
  times = info["hourly"]["time"]
  wave_height = info["hourly"]["wave_height"]

  wave_height = [
      {"datetime": t, "wave_height": s}
      for t, s in zip(times, wave_height)
  ]

  return {"sea wave height": wave_height}

@app.get("/get-climate-temp")
def temp():
  url = "https://api.open-meteo.com/v1/forecast?latitude=34.052235&longitude=124.5085&hourly=temperature_2m"

  climateTemp = requests.get(url).json()

  return {"sea temp": climateTemp}

@app.get("/get-global-temp")
def temp():
  url = "https://global-warming.org/api/temperature-api"

  globalTemp = requests.get(url).json()

  return {"sea temp": globalTemp}

@app.get("/get-carbon-dioxide")
def temp():
  url = "https://global-warming.org/api/co2-api"

  globalTemp = requests.get(url).json()

  return {"sea temp": globalTemp}

@app.get("/get-methane")
def temp():
  url = "https://global-warming.org/api/methane-api"

  globalTemp = requests.get(url).json()

  return {"sea temp": globalTemp}

@app.get("/get-nitrous-oxide")
def temp():
  url = "https://global-warming.org/api/nitrous-oxide-api"

  globalTemp = requests.get(url).json()

  return {"sea temp": globalTemp}

@app.get("/get-polar-ice")
def temp():
  url = "https://global-warming.org/api/arctic-api"

  globalTemp = requests.get(url).json()

  return {"sea temp": globalTemp}

@app.get("/get-ocean-warming")
def temp():
  url = "https://global-warming.org/api/ocean-warming-api"

  globalTemp = requests.get(url).json()

  return {"sea temp": globalTemp}