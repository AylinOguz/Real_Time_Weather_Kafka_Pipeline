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

  ## How to Run the Project

### Install Dependencies

- Create a virtual environment:

python -m venv .venv


- Activate it (Windows PowerShell):

.venv\Scripts\activate


- Install required Python packages:

pip install -r requirements.txt

### Start Kafka

- If you are using Docker:

docker-compose up -d


If Kafka is installed locally, make sure these services are running:

Zookeeper → localhost:2181

Kafka Broker → localhost:9092

### Set Environment Variables

In PowerShell:

$env:WEATHER_API_KEY="your_api_key"
$env:MYSQL_PASSWORD="your_mysql_password"

### Start MySQL and Create the Database

Run the following command in MySQL:

CREATE DATABASE weather_db;

The consumer script will automatically create the table if it doesn’t exist.

### Run the Producer

- Fetches real-time weather data from WeatherAPI and sends it to the Kafka topic:

python producer.py


- Expected output:

Sent: {'city': 'Istanbul', 'temp_c': 12.3, ...}

### Run the Consumer

Consumes messages from Kafka and writes them to MySQL and CSV:

python consumer.py


Example output:

Inserted into MySQL: {...}
Appended to CSV: weather_data_sample.csv

### Verify the Results
✔ MySQL Database
USE weather_db;
SELECT * FROM weather;

✔ CSV File

A CSV file will automatically appear in your project folder:

weather_data_sample.csv



