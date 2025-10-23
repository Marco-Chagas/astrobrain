from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from kerykeion import Kerykeion

app = FastAPI()

# Permite que o Lovable ou seu app web acessem este backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/natal")
def get_natal_chart(name: str, year: int, month: int, day: int, hour: int, minute: int, lat: float, lon: float, tz: float):
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
