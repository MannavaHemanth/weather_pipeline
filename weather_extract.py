#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import psycopg2
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Configuration from .env
API_KEY = os.getenv("API_KEY")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_data (
        id SERIAL PRIMARY KEY,
        city VARCHAR(50),
        temperature FLOAT,
        humidity INT,
        timestamp TIMESTAMP
    );
''')

# Loop through each city
for city in cities:
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            timestamp = datetime.now()

            cursor.execute('''
                INSERT INTO weather_data (city, temperature, humidity, timestamp)
                VALUES (%s, %s, %s, %s)
            ''', (city, temperature, humidity, timestamp))

            print(f"✅ {city} | Temp: {temperature}°C | Humidity: {humidity}%")

        else:
            print(f"⚠️ Failed to fetch data for {city}: {data.get('message', 'Unknown error')}")

    except Exception as e:
        print(f"❌ Error for {city}: {e}")

# Finalize
conn.commit()
cursor.close()
conn.close()
print("🔒 All data committed and DB connection closed.")

