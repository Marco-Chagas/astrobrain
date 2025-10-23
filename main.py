from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from kerykeion import Kerykeion

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AstroBrain API online — consulte /natal para gerar seu mapa astral"}

@app.get("/natal")
def get_natal_chart(
    name: str,
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int,
    lat: float,
    lon: float,
    tz: float
):
    try:
        k = Kerykeion(
            name=name,
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            lat=lat,
            lon=lon,
            tz=tz
        )
        return {
            "sun": k.sun.sign,
            "moon": k.moon.sign,
            "ascendant": k.ascendant.sign
        }
    except Exception as e:
        return {"error": str(e)}

