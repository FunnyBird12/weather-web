from string import ascii_uppercase
from typing import Annotated
from fastapi import FastAPI
from fastapi.params import Query
from starlette.requests import Request
import httpx
from fastapi.templating import Jinja2Templates
from models import ApiResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
template = Jinja2Templates(directory="frontend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home(request:Request):
    return template.TemplateResponse(
        "main.html",
        {"request": request}
    )


@app.get("/weather")
async def response(city:str,today:str):
    API_KEY = "K8NZJ2PGQBYFYAHX6VXBD3CJY"
    URL = (f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/"f"timeline/{city}/{today}/{today}"f"?unitGroup=metric&key={API_KEY}&contentType=json")

    async with httpx.AsyncClient() as client:
        res = await client.get(URL)
        print(res.status_code)  # ← смотри в терминале
        print(res.text)  # ← смотри что вернул API
    return res.json()