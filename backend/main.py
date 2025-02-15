
from fastapi import FastAPI
from routes import grants, businesses, outreach

app = FastAPI()

app.include_router(grants.router)
app.include_router(businesses.router)
app.include_router(outreach.router)

@app.get("/")
def read_root():
    return {"message": "Grant Matching API is running"}
