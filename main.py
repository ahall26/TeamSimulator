import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from scripts.create_team import create_team

app = FastAPI()


@app.get("/")
async def read_root():
    headers = {"Access-Control-Allow-Origin": "*"}
    team = json.dumps({"team": create_team()})
    return JSONResponse(content=team, headers=headers)
