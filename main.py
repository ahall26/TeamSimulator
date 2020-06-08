import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from scripts.create_team import create_team

app = FastAPI()


@app.get("/")
async def read_root():
    headers = {"Access-Control-Allow-Origin": "*"}
    team = json.dumps({"team": create_team()})
    print(team)
    content = team
    return JSONResponse(content=content, headers=headers)
