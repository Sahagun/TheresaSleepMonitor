import board
import adafruit_sht4x
import adafruit_veml7700

# Instantiate sensor objects
veml7700 = adafruit_veml7700.VEML7700(board.I2C()) # Light Sensor
sht = adafruit_sht4x.SHT4x(board.I2C()) # Temp and Hum Sensor


# How to use
print("Temperature", sht.temperature)
print("Humidity",sht.relative_humidity)
print("Ambient light:", veml7700.light)
print("Lux:", veml7700.lux)
