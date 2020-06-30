import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from scripts.create_team import create_team, Team, update_member

app = FastAPI()

headers = {"Access-Control-Allow-Origin": "*"}


@app.get("/")
async def generate_team(team_size: int = 3, team_role: str = "", team_company: str = "", team_name: str = ""):
    team = json.dumps(
        {"team": create_team(team_size=team_size, team_role=team_role, team_name=team_name, team_company=team_company)})
    return JSONResponse(content=team, headers=headers)


@app.get("/updatemember")
async def generate_team(team_size: int = 3, team_role: str = "", team_company: str = "", team_name: str = ""):
    return JSONResponse(content=update_member, headers=headers)

@app.get("/roles")
async def get_roles():
    return JSONResponse(content=list(Team.job_titles), headers=headers)

@app.get("/personalities")
async def get_personality_types():
    return JSONResponse(content=Team.personality_types, headers=headers)


@app.get("/compatibilities")
async def get_compatibilities():
    return JSONResponse(content=Team.personality_comp, headers=headers)
