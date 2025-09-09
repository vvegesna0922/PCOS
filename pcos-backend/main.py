from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Connect to the same SQLite database
conn = sqlite3.connect("pcos_tracker.db", check_same_thread=False)
cursor = conn.cursor()

# Pydantic model for data validation
class HealthData(BaseModel):
    date: str
    period_length: int
    symptoms: str
    mood: str

# POST endpoint to add new data
@app.post("/add")
def add_health_data(data: HealthData):
    cursor.execute(
        "INSERT INTO health_data (date, period_length, symptoms, mood) VALUES (?, ?, ?, ?)",
        (data.date, data.period_length, data.symptoms, data.mood)
    )
    conn.commit()
    return {"message": "Data added successfully!"}

# GET endpoint to fetch all data
@app.get("/all")
def get_all_data():
    cursor.execute("SELECT * FROM health_data")
    rows = cursor.fetchall()
    return {"data": rows}

@app.get("/")
def root():
    return {"message": "Welcome to the PCOS Health Tracker API!"}
