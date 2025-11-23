from kafka import KafkaConsumer
import json
import mysql.connector
import os
import pandas as pd

# Get MySQL password from environment variable
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
if not MYSQL_PASSWORD:
    raise ValueError("MYSQL_PASSWORD not found! Check your environment variable or .env file.")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=MYSQL_PASSWORD,
    database="weather_db"
)
cursor = conn.cursor()

# Create table (use weather_condition because "condition" is a MySQL keyword)
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    temp_c FLOAT,
    humidity FLOAT,
    weather_condition VARCHAR(50),
    timestamp VARCHAR(50)
)
""")
conn.commit()

# Kafka consumer
consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='latest'
)

CSV_FILE = "weather_data_sample.csv"

for message in consumer:
    data = message.value

    # Insert into MySQL
    cursor.execute("""
        INSERT INTO weather (city, temp_c, humidity, weather_condition, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        data.get("city"),
        data.get("temp_c"),
        data.get("humidity"),
        data.get("condition"),
        data.get("timestamp")
    ))
    conn.commit()
    print("Inserted into MySQL:", data)

    # Append to CSV
    df = pd.DataFrame([data])
    df.to_csv(
        CSV_FILE,
        mode='a',
        header=not os.path.exists(CSV_FILE),
        index=False
    )
    print(f"Appended to CSV: {CSV_FILE}")
