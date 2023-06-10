import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
import board
import adafruit_sht4x
import adafruit_veml7700

# Create an ID for this raspberry pi
deviceID = 'abc123'

# Instantiate sensor objects
veml7700 = adafruit_veml7700.VEML7700(board.I2C()) # Light Sensor
sht = adafruit_sht4x.SHT4x(board.I2C()) # Temp and Hum Sensor


# Fetch the service account key JSON file contents
cred = credentials.Certificate('firebase_key.json')

# Initialize the app with a service account, granting admin privileges
# Update 'databaseURL' to your database url
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://homeweatherstation-de4f2-default-rtdb.firebaseio.com',
#    'databaseURL': 'https://YOURPROJECTPATHHERE.firebaseio.com',
	'databaseAuthVariableOverride': {
        'uid': 'admin'
    }
})


# Create a refernce to the data base with the path for the device
ref = db.reference('devices/%s'%deviceID)
ts = str(int(time.time() * 1000))
new_entry_ref = ref.child(ts)
new_entry_ref.set({
    'Temperature': sht.temperature,
    'Humidity': sht.relative_humidity,
    'AmbientLight': veml7700.light,
    'Lux': veml7700.lux
    
})

print('done')
