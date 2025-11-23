# Real-Time Weather Data Pipeline with Kafka
This project demonstrates a real-time data engineering pipeline that collects weather data from an external API and streams it through Apache Kafka, then stores it into a MySQL database and simultaneously exports it to a CSV file for analysis.
## Project Architecture
Weather API → Producer → Kafka Topic → Consumer → MySQL + CSV

### Producer

- Fetches weather data every 60 seconds from WeatherAPI.

- Sends simplified JSON messages to Kafka (sensor-data topic).

### Consumer

- Listens to Kafka messages in real-time.

- Inserts each record into MySQL.

- Appends the same record to weather_data_sample.csv.
