#!/usr/bin/env python3

import Adafruit_DHT
import time
import datetime
import mysql.connector
import RPi.GPIO as GPIO
import asyncio
import websockets
import threading

# Set the DHT sensor types and GPIO pins
DHT_SENSOR_1 = Adafruit_DHT.DHT22
DHT_SENSOR_2 = Adafruit_DHT.DHT22
DHT_PIN_1 = 21
DHT_PIN_2 = 22

# Database credentials
db_config = {
    "host": "192.168.0.221",
    "user": "root",
    "password": "root",
    "database": "Temperature_Sensor"
}

# Global variable to control data gathering
gather_data = False

async def server(websocket, path):
    global gather_data
    command = await websocket.recv()
    print(f"< {command}")

    if command == "start":
        gather_data = True
    elif command == "stop":
        gather_data = False

start_server = websockets.serve(server, "192.168.0.221", 8765)

def read_dht_sensor(sensor_id, dht_pin):
    try:
        # Read the temperature and humidity from the DHT sensor
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR_1 if sensor_id == 1 else DHT_SENSOR_2, dht_pin)
        if humidity is not None and temperature is not None:
            # Get the current timestamp
            current_time = datetime.datetime.now()

            # Insert data into the database
            insert_data_into_database(current_time, temperature, humidity, "DHT22_" + str(sensor_id))
        else:
            print(f"Failed to retrieve data from DHT22_{sensor_id} sensor. Check your connections.")
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)
    except Exception as e:
        print(f"Error occurred: {e}")

def insert_data_into_database(timestamp, temperature, humidity, sensor_name):
    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # SQL queries to insert data into Temperature and Humidity tables
        temperature_query = "INSERT INTO `Temperature` (`Temperature_ID`, `Temperature_Value`, `Sensor_ID`, `Room_ID`, `Date_of_reading`) " \
                            "VALUES (%s, %s, %s, %s, %s)"

        humidity_query = "INSERT INTO `Humidity` (`Humidity_ID`, `Humidity_Value`, `Sensor_ID`, `Room_ID`, `Date_of_reading`) " \
                         "VALUES (%s, %s, %s, %s, %s)"

        temperature_id = None 
        humidity_id = None
        room_id = 1  

        temperature_data = (temperature_id, temperature, sensor_id, room_id, timestamp)
        humidity_data = (humidity_id, humidity, sensor_id, room_id, timestamp) 
        
        cursor.execute(temperature_query, temperature_data)
        cursor.execute(humidity_query, humidity_data)

        # Commit the changes to the database
        connection.commit()

        print("Data inserted into the database successfully.")
    except Exception as e:
        print(f"Error occurred while inserting data: {e}")
    finally:
        # Close the database connection
        cursor.close()
        connection.close()


if __name__ == "__main__":
    sensor_id = 1
    try:
        # Start the websocket server in a new thread
        websocket_thread = threading.Thread(target=asyncio.get_event_loop().run_until_complete, args=(start_server,))
        websocket_thread.start()

        while True:
            if gather_data:
                current_time = datetime.datetime.now()

                if sensor_id == 1:
                    read_dht_sensor(sensor_id, DHT_PIN_1)
                else:
                    read_dht_sensor(sensor_id, DHT_PIN_2)

                # Update time every second
                time.sleep(0.5)

                # Toggle between sensor 1 and sensor 2 every 10 seconds
                if current_time.second % 10 == 0:
                    sensor_id = 2 if sensor_id == 1 else 1
    except KeyboardInterrupt:
        print("Script stopped by the user.")
    finally:
        # Cleanup GPIO on exit
        GPIO.cleanup()
