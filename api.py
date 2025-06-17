#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI
import psycopg2
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Database connection settings
DB_PARAMS = {
    "dbname": "weather_db",
    "user": "postgres",
    "password": "Hemanth@19",  # Replace with your password
    "host": "localhost",
    "port": "5432"
}

# Pydantic model
class WeatherData(BaseModel):
    city: str
    temperature: float
    humidity: int
    timestamp: str

@app.get("/")
def read_root():
    return {"message": "🌤️ Weather API is up and running!"}

@app.get("/weather", response_model=List[WeatherData])
def get_weather_data():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("SELECT city, temperature, humidity, timestamp FROM weather_data ORDER BY timestamp DESC LIMIT 10;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [
        {"city": row[0], "temperature": row[1], "humidity": row[2], "timestamp": str(row[3])}
        for row in rows
    ]

