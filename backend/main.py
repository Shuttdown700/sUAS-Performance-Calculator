from fastapi import FastAPI
from routers.router_load_json_data import router as json_data_router

app = FastAPI()

# Include routers
app.include_router(json_data_router)

@app.get("/")
def root():
    return {"message": "Drone Flight Calculator API is running"}
