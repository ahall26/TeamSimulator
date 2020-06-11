import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from scripts.create_team import create_team

app = FastAPI()
job_titles = list({"Accountant": "Office Worker", "Actor": "Actor", "Administrator": "Technologist", "Artist": "Artist",
                   "Athletic Coach": "Teacher", "Banker": "Technologist", "Bookkeeper": "Teacher",
                   "Business Analyst": "Office Worker", "Business Manager": "Office Worker", "Carpentry": "Mechanic",
                   "Chef": "Cook", "Child Care Provider": "Childcare", "Childcare": "Childcare",
                   "Company Ceo Or Manager": "Office Worker", "Composer Or Musician": "Singer",
                   "Computer Programming": "Technologist", "Computer Support Technician": "Technologist",
                   "Counseling": "Counselor", "Counselor": "Counselor", "Dentist": "Health Worker",
                   "Designer": "Artist",
                   "Detectives": "Detective", "Doctor": "Health Worker", "Electrician": "Mechanic",
                   "Engineer": "Factory Worker", "Engineering": "Factory Worker", "Entrepreneur": "Office Worker",
                   "Fashion Designer": "Artist", "Firefighter": "Firefighter", "Forensic Science": "Scientist",
                   "Forest Ranger": "Police Officer", "Graphic Designer": "Office Worker",
                   "Human Resources Manager": "Office Worker", "Human Resources Specialist": "Office Worker",
                   "Inventor": "Scientist", "Journalist": "Detective", "Judge": "Judge",
                   "Law Enforcement": "Police Officer", "Lawyer": "Office Worker", "Librarian": "Teacher",
                   "Manager": "Office Worker", "Marketer": "Office Worker", "Mathematician": "Teacher",
                   "Mechanics": "Mechanic", "Military": "Pilot", "Musician": "Singer", "Naturalist": "Farmer",
                   "Nurse": "Health Worker", "Nursing": "Health Worker", "Nutritionist": "Health Worker",
                   "Office Manager": "Office Worker", "Paralegal": "Office Worker", "Paramedic": "Health Worker",
                   "Pediatrician": "Health Worker", "Photographer": "Detective", "Physical Therapist": "Health Worker",
                   "Physician": "Health Worker", "Pilot": "Pilot", "Police Officer": "Police Officer",
                   "Police Officers": "Police Officer", "Politician": "Office Worker", "Psychiatrist": "Health Worker",
                   "Psychologist": "Health Worker", "Receptionist": "Technologist", "Religious Worker": "Pilot",
                   "Sales Agent": "Office Worker", "Sales Representative": "Office Worker",
                   "School Administrator": "Teacher", "Scientist": "Scientist", "Social Work": "Teacher",
                   "Social Worker": "Teacher", "Software Developer": "Technologist",
                   "Software Engineer": "Technologist",
                   "Teacher": "Teacher", "Teaching": "Teacher", "Tv Anchor/Reporter": "Office Worker",
                   "University Professor": "Teacher", "Veterinarian": "Health Worker",
                   "Video Game Designer": "Technologist", "Writer": "Technologist"})

headers = {"Access-Control-Allow-Origin": "*"}


@app.get("/")
async def generate_team(team_size: int = 2, team_role: str = "", team_company: str = "", team_name: str = ""):
    team = json.dumps(
        {"team": create_team(team_size=team_size, team_role=team_role, team_name=team_name, team_company=team_company)})
    return JSONResponse(content=team, headers=headers)


@app.get("/roles")
async def get_roles():
    print(job_titles)
    return JSONResponse(content=job_titles, headers=headers)
