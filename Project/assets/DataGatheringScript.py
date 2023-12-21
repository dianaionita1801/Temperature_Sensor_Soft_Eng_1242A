#!/usr/bin/env python3

import Adafruit_DHT
import time
import datetime
import mysql.connector
import subprocess
import RPi.GPIO as GPIO

""" import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# OLED display I2C address (you may need to change this based on your display)
# OLED_I2C_ADDR = 0x3C
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
# Initialize the OLED display with I2C interface
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library
disp.begin()

# Clear display
disp.clear()
disp.display() """

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

""" # Function to display text on the OLED screen
def display_on_oled(text_lines):
    # Create an image with mode '1' for 1-bit color (black and white)
    image = Image.new('1', (disp.width, disp.height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Clear the display
    draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)

    # Draw each line of text on the screen
    line_height = 8
    y = 0
    for line in text_lines:
        draw.text((0, y), line, font=font, fill=255)
        y += line_height

    # Display the image
    disp.image(image)
    disp.display() """

def read_dht_sensor(sensor_id, dht_pin):
    try:
        # Read the temperature and humidity from the DHT sensor
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR_1 if sensor_id == 1 else DHT_SENSOR_2, dht_pin)
        if humidity is not None and temperature is not None:
            # Get the current timestamp
            current_time = datetime.datetime.now()
            """ temperature_text = f"Temperature: {temperature:.2f} °C"
            humidity_text = f"Humidity: {humidity:.2f}%" """
            insert_data_into_database(current_time, temperature, humidity, "DHT22_" + str(sensor_id))
            
            """ # Prepare the lines of text to display
            text_lines = [
                "IP: " + get_ip_address(),
                "Sensor: DHT22_" + str(sensor_id),
                temperature_text,
                humidity_text,
                "Room ID: 1",
                current_time.strftime("%Y/%m/%d")+" "+current_time.strftime("%H:%M:%S")
            ]
            
            # Print the values on the OLED screen
            display_on_oled(text_lines) """

            # Insert data into the database
        else: 
            print(f"Failed to retrieve data from DHT22_{sensor_id} sensor. Check your connections.")
        
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)
    except Exception as e:
        print(f"Error occurred: {e}")

""" def get_ip_address():
    # Shell command to get the IP address of the Raspberry Pi
    cmd = "hostname -I | cut -d' ' -f1"
    return subprocess.check_output(cmd, shell=True).decode("utf-8").strip() """

def insert_data_into_database(timestamp, temperature, humidity, sensor_name):
    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Prepare the SQL queries to insert data into Temperature and Humidity tables
        temperature_query = "INSERT INTO `Temperature` (`Temperature_ID`, `Temperature_Value`, `Sensor_ID`, `Room_ID`, `Date_of_reading`) " \
                            "VALUES (%s, %s, %s, %s, %s)"

        humidity_query = "INSERT INTO `Humidity` (`Humidity_ID`, `Humidity_Value`, `Sensor_ID`, `Room_ID`, `Date_of_reading`) " \
                         "VALUES (%s, %s, %s, %s, %s)"

        # Values to be inserted into the database (modify these as needed)
        temperature_id = None  # If you have an auto-incrementing primary key, set this to None
        humidity_id = None
        room_id = 1  # Replace with the appropriate room ID

        # Execute the SQL queries with the data
        temperature_data = (temperature_id, temperature, sensor_id, room_id, timestamp)
        humidity_data = (humidity_id, humidity, sensor_id, room_id, timestamp)  # If you have an auto-incrementing primary key for Humidity, set this to None

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

# Main loop to continuously read the sensor data
if __name__ == "__main__":
    sensor_id = 1
    try:
        while True:
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