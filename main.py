from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from kerykeion import astrological_subject_factory

app = FastAPI()

# Enable CORS for universal access
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
        # Instantiate the factory correctly
        factory = astrological_subject_factory.AstrologicalSubjectFactory(
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

        # Build the subject
        subject = factory.build()

        # Return key positions
        return {
            "sun": subject.sun.sign,
            "moon": subject.moon.sign,
            "ascendant": subject.ascendant.sign
        }
    except Exception as e:
        return {"error": str(e)}
