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

@app.get("/get-forecast-temp")
def forecastTemp():
  url = "https://api.open-meteo.com/v1/forecast?latitude=34.052235&longitude=124.5085&hourly=temperature_2m"

  info = requests.get(url).json()
  times = info["hourly"]["time"]
  temp = info["hourly"]["temperature_2m"]

  temp = [
      {"datetime": t, "temperature_2m": s}
      for t, s in zip(times, temp)
  ]

  return {"temperature": temp}

@app.get("/get-global-temp")
def globalTemp():
  url = "https://global-warming.org/api/temperature-api"
  info = requests.get(url).json()

  data = info["result"] 
  temp_1800s = [entry for entry in data if entry["time"].startswith("18")]
  temp_1900s = [entry for entry in data if entry["time"].startswith("19")]
  temp_2000s = [entry for entry in data if entry["time"].startswith("20")]
  temp_2025s = [entry for entry in data if entry["time"].startswith("2025")]

  return {
        "1800s": temp_1800s[0],
        "1900s": temp_1900s[0],
        "2000s": temp_2000s[0],
        "2025": temp_2025s[0]
    }

@app.get("/get-carbon-dioxide")
def co2():
  url = "https://global-warming.org/api/co2-api"
  info = requests.get(url).json()

  data = info["co2"] 
  co2015s = [entry for entry in data if entry["year"].startswith("2015")]
  co2025s = [entry for entry in data if entry["year"].startswith("2025")]

  return {
        "2015s": co2015s[0],
        "2025s": co2025s[0],
    }

@app.get("/get-methane")
def methane():
  url = "https://global-warming.org/api/methane-api"

  info = requests.get(url).json()

  data = info["methane"] 
  methane1984s = [entry for entry in data if entry["date"].startswith("1984")]
  methane2000s = [entry for entry in data if entry["date"].startswith("2000")]
  methane2015s = [entry for entry in data if entry["date"].startswith("2015")]
  methane2025s = [entry for entry in data if entry["date"].startswith("2025")]

  return {
        "1984s": methane1984s[0],
        "200s": methane2000s[0],
        "2015s": methane2015s[0],
        "2025s": methane2025s[0],
    }

@app.get("/get-nitrous-oxide")
def nitrousOxide():
  url = "https://global-warming.org/api/nitrous-oxide-api"

  info = requests.get(url).json()

  data = info["nitrous"] 
  nitrousOxide2002s = [entry for entry in data if entry["date"].startswith("2002")]
  nitrousOxide2015s = [entry for entry in data if entry["date"].startswith("2015")]
  nitrousOxide2025s = [entry for entry in data if entry["date"].startswith("2025")]

  return {
        "2002s": nitrousOxide2002s[0],
        "2015s": nitrousOxide2015s[0],
        "2025s": nitrousOxide2025s[0],
    }