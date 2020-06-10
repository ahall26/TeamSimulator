import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from scripts.create_team import create_team

app = FastAPI()


@app.get("/")
async def generate_team(team_size: int = 3):
    headers = {"Access-Control-Allow-Origin": "*"}
    team = json.dumps({"team": create_team(team_size=team_size)})
    return JSONResponse(content=team, headers=headers)
