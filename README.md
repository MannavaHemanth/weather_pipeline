# 🌦️ Weather Data Pipeline Project

This project:
- Fetches real-time weather data from the OpenWeatherMap API for multiple cities
- Stores the data in a PostgreSQL database
- Is scheduled to run automatically (via Windows Task Scheduler or cron)
- (Optionally) exposes the data via FastAPI

## 🔧 Tech Stack
- Python
- PostgreSQL
- OpenWeatherMap API
- Task Scheduler / Cron (for automation)
- FastAPI (optional)

## 🚀 How to Run
1. Clone the repo
2. Set up a `.env` file with:
    ```
    API_KEY=your_key_here
    DB_NAME=weather_db
    DB_USER=postgres
    DB_PASSWORD=your_password
    DB_HOST=localhost
    DB_PORT=5432
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the script:
    ```bash
    python weather_extract.py
    ```

## ✅ Output Example
✅ London | Temp: 22.3°C | Humidity: 55%
✅ Chennai | Temp: 31.0°C | Humidity: 70%

This script is scheduled to run every day using Windows Task Scheduler.
