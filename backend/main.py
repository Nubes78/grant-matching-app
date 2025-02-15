  
from fastapi import FastAPI, Query  
from typing import List  

app = FastAPI()  

grants_db = [
    {"id": 1, "title": "AI Research Grant", "technology": "Artificial Intelligence"},
    {"id": 2, "title": "Renewable Energy Fund", "technology": "Solar Energy"},
    {"id": 3, "title": "Cybersecurity Innovation", "technology": "Cybersecurity"}
]

businesses_db = [
    {"id": 1, "name": "AI Corp", "industry": "Artificial Intelligence", "ceo": "Alice Johnson", "email": "alice@aicorp.com"},
    {"id": 2, "name": "Green Energy Inc.", "industry": "Solar Energy", "ceo": "Bob Smith", "email": "bob@greenenergy.com"},
    {"id": 3, "name": "SecureTech", "industry": "Cybersecurity", "ceo": "Charlie Lee", "email": "charlie@securetech.com"}
]

@app.get("/")  
def read_root():  
    return {"message": "Grant Matching API is running"}  

@app.get("/grants/")  
def get_grants():  
    return grants_db  

@app.get("/businesses/")  
def get_businesses():  
    return businesses_db  

@app.get("/match/grant/{grant_id}")  
def match_grant_to_businesses(grant_id: int):  
    grant = next((g for g in grants_db if g["id"] == grant_id), None)
    if not grant:
        return {"error": "Grant not found"}
    
    matches = [b for b in businesses_db if b["industry"] == grant["technology"]]
    return {"grant": grant, "matching_businesses": matches}  

@app.get("/match/business/{business_id}")  
def match_business_to_grants(business_id: int):  
    business = next((b for b in businesses_db if b["id"] == business_id), None)
    if not business:
        return {"error": "Business not found"}
    
    matches = [g for g in grants_db if g["technology"] == business["industry"]]
    return {"business": business, "matching_grants": matches}  
