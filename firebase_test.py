import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time

# Fetch the service account key JSON file contents
cred = credentials.Certificate('firebase_key.json')

# Initialize the app with a service account, granting admin privileges
# Update 'databaseURL' to your database url
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://YOURPROJECTPATHHERE.firebaseio.com',
	'databaseAuthVariableOverride': {
        'uid': 'admin'
    }
})


# Create an ID for this raspberry pi
deviceID = 'abc123'

# Create a refernce to the data base with the path for the device
ref = db.reference('devices/%s'%deviceID)
# Create a timestamp
ts = str(int(time.time()))
# A new ref for the timestamp
new_entry_ref = ref.child(ts)
# Here you can set a json object to the database
new_entry_ref.set({
    'temperature': 23.45
})


# Read from the data saved to your device's path from the database
print(ref.get())
