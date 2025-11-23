# Real-Time Weather Data Pipeline with Kafka
This project demonstrates a real-time data engineering pipeline that collects weather data from an external API and streams it through Apache Kafka, then stores it into a MySQL database and simultaneously exports it to a CSV file for analysis.
## Project Architecture
Weather API → Producer → Kafka Topic → Consumer → MySQL + CSV
