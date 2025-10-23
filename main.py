from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from kerykeion.charts import AstrologicalSubject

app = FastAPI()

# Middleware for CORS
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
        person = AstrologicalSubject(
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

        # The signs are now accessible like this in Kerykeion 5.x
        return {
            "sun": person.sun.sign,
            "moon": person.moon.sign,
            "ascendant": person.ascendant.sign
        }
    except Exception as e:
        return {"error": str(e)}
