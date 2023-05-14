# Programmed by DabCat

"""
This program will monitor grow tent conditions such as temperature
and humidity. The program operates via a Rasberry Pi board interface
connected to a thermometer and hydrometer.
"""

import Adafruit_DHT.common as cm

# Set platform to UNKNOWN to avoid "/proc/cpuinfo" error
cm.PLATFORM = "UNKNOWN"

# Use DHT11 or DHT20 sensor and pin number
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

# Read and Display Temp and Dew values
while True:
    dew, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if dew is not None and temp is not None:
        print(f"Temperature: {temp:.1f} °C, Humidity: {dew:.1f} %")
    else:
        print("Failed to fetch data from sensors. Check Cables.")