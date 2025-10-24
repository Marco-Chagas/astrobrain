from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kerykeion import KrInstance
import pytz

app = FastAPI(title="AstroBrain API", description="Accurate Swiss Ephemeris-based Natal Chart API")

class NatalData(BaseModel):
    name: str
    year: int
    month: int
    day: int
    hour: int
    minute: int
    lat: float
    lon: float
    timezone: float

@app.get("/")
def root():
    return {"status": "✅ AstroBrain is online and ready for POST /natal_chart"}

@app.post("/natal_chart")
def natal_chart(data: NatalData):
    try:
        # Create the instance
        kr = KrInstance(
            name=data.name,
            year=data.year,
            month=data.month,
            day=data.day,
            hour=data.hour,
            minute=data.minute,
            lon=data.lon,
            lat=data.lat,
            tz=data.timezone
        )

        # Build the response
        return {
            "name": data.name,
            "sun": kr.sun,
            "moon": kr.moon,
            "ascendant": kr.ascendant,
            "planets": kr.planets,
            "houses": kr.houses,
            "aspects": kr.aspects
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
