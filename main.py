import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from scripts.create_team import create_team

app = FastAPI()
job_titles = list({
    "Accountant": "Office Worker",
    "Actor": "Actor",
    "Administrator": "Technologist",
    "Artist": "Artist",
    "Athletic coach": "Teacher",
    "Banker": "Technologist",
    "Bookkeeper": "Teacher",
    "Business analyst": "Office Worker",
    "Business manager": "Office Worker",
    "Carpentry": "Mechanic",
    "Chef": "Cook",
    "Child care provider": "Childcare",
    "Childcare": "Childcare",
    "Company CEO or manager": "Office Worker",
    "Composer or musician": "Singer",
    "Computer programming": "Technologist",
    "Computer support technician": "Technologist",
    "Counseling": "Counselor",
    "Counselor": "Counselor",
    "Dentist": "Health Worker",
    "Designer": "Artist",
    "Detectives": "Detective",
    "Doctor": "Health Worker",
    "Electrician": "Mechanic",
    "Engineer": "Factory Worker",
    "Engineering": "Factory Worker",
    "Entrepreneur": "Office Worker",
    "Fashion designer": "Artist",
    "Firefighter": "Firefighter",
    "Forensic science": "Scientist",
    "Forest ranger": "Police Officer",
    "Graphic Designer": "Office Worker",
    "Human resources manager": "Office Worker",
    "Human resources specialist": "Office Worker",
    "Inventor": "Scientist",
    "Journalist": "Detective",
    "Judge": "Judge",
    "Law enforcement": "Police Officer",
    "Lawyer": "Office Worker",
    "Librarian": "Teacher",
    "Manager": "Office Worker",
    "Marketer": "Office Worker",
    "Mathematician": "Teacher",
    "Mechanics": "Mechanic",
    "Military": "Pilot",
    "Musician": "Singer",
    "Naturalist": "Farmer",
    "Nurse": "Health Worker",
    "Nursing": "Health Worker",
    "Nutritionist": "Health Worker",
    "Office Manager": "Office Worker",
    "Paralegal": "Office Worker",
    "Paramedic": "Health Worker",
    "Pediatrician": "Health Worker",
    "Photographer": "Detective",
    "Physical Therapist": "Health Worker",
    "Physician": "Health Worker",
    "Pilot": "Pilot",
    "Police officer": "Police Officer",
    "Police officers": "Police Officer",
    "Politician": "Office Worker",
    "Psychiatrist": "Health Worker",
    "Psychologist": "Health Worker",
    "Receptionist": "Technologist",
    "Religious worker": "Pilot",
    "Sales agent": "Office Worker",
    "Sales representative": "Office Worker",
    "School administrator": "Teacher",
    "Scientist": "Scientist",
    "Social work": "Teacher",
    "Social Worker": "Teacher",
    "Software developer": "Technologist",
    "Software engineer": "Technologist",
    "Teacher": "Teacher",
    "Teaching": "Teacher",
    "TV Anchor/Reporter": "Office Worker",
    "University professor": "Teacher",
    "Veterinarian": "Health Worker",
    "Video game designer": "Technologist",
    "Writer": "Technologist"
})

headers = {"Access-Control-Allow-Origin": "*"}


@app.get("/")
async def generate_team(team_size: int = 3):
    team = json.dumps({"team": create_team(team_size=team_size)})
    return JSONResponse(content=team, headers=headers)


@app.get("/roles")
async def get_roles():
    print(job_titles)
    return JSONResponse(content=job_titles, headers=headers)
