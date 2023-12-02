from bluepy.btle import Peripheral, UUID, DefaultDelegate
import requests
message_url = 'http://192.168.1.134:5000/message'
heart_rate_url ='http://192.168.1.134:5000/heart_rate'
hr_url ='http://192.168.1.134:5000/hr'
age = 53
class HeartRateDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        # This function is called when a notification is received
        if cHandle == self.heart_rate_handle:
            # Extract the heart rate value from the notification and print it
            heart_rate = abs(int.from_bytes(data[1 : 1 + 8], byteorder="little", signed=True))
            heartrate = heart_rate
            hr = str (heart_rate)
            send_heart_rate(heartrate) 
            send_hr(hr)
            print("Heart rate: {} bpm".format(heart_rate))
            if heart_rate > (220-age)*0.85:
              message = 'Slow down'
              send_message(message)
              
            elif (220-age)*0.85>= heart_rate >=(220-age)*0.50:
                message = 'Normal'
                send_message(message)
                
            elif heart_rate < (220-age)*0.50:
                message = 'Speed up'
                send_message(message)
                
        elif cHandle == self.battery_level_handle:
            # Extract the battery level value from the notification and print it
            battery_level = int.from_bytes(data, byteorder="little")
            print("Battery level: {}%".format(battery_level))

class VeritySenseSensor:
    def __init__(self, mac_address):
        self.peripheral = Peripheral(mac_address)
        self.heart_rate_uuid = UUID("00002a37-0000-1000-8000-00805f9b34fb")
        self.battery_level_uuid = UUID("00002a19-0000-1000-8000-00805f9b34fb")
        self.heart_rate_handle = self.peripheral.getCharacteristics(uuid=self.heart_rate_uuid)[0].getHandle()
        self.battery_level_handle = self.peripheral.getCharacteristics(uuid=self.battery_level_uuid)[0].getHandle()
        self.heart_rate_delegate = HeartRateDelegate()
        self.heart_rate_delegate.heart_rate_handle = self.heart_rate_handle
        self.heart_rate_delegate.battery_level_handle = self.battery_level_handle
        self.peripheral.withDelegate(self.heart_rate_delegate)

    def enable_notifications(self):
        # Enable notifications for the heart rate characteristic
        self.peripheral.writeCharacteristic(self.heart_rate_handle + 1, b"\x01\x00")
        # Enable notifications for the battery level characteristic
        self.peripheral.writeCharacteristic(self.battery_level_handle + 1, b"\x01\x00")

    def read_battery_level(self):
        # Read the battery level characteristic
        battery_level_value = self.peripheral.readCharacteristic(self.battery_level_handle)
        battery_level = int.from_bytes(battery_level_value, byteorder="little")
        return battery_level

    def disconnect(self):
        # Disconnect from the sensor
        self.peripheral.disconnect()
        
def send_heart_rate(heart_rate):     
	# Send heart rate to the Flask server
	
	data = {'heart_rate': heart_rate}
	response = requests.post(heart_rate_url, data=data)

	# Check the response status
	if response.status_code == 200:
	    print('Heart rate sent successfully')
	else:
	    print('Failed to send heart rate')
def send_hr(hr):     
	# Send heart rate to the Flask server
        data = {'hr': hr}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(hr_url, json=data, headers=headers)
        return True
	
def send_message(message):
    data = {'message': message}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(message_url, json=data, headers=headers)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print("Failed to send message")

def get_heart_rate_and_battery_level():
    # Specify the MAC address of the Polar Verity Sense sensor
    mac_address = "A0:9E:1A:91:4B:51"

    # Connect to the sensor and enable notifications
    sensor = VeritySenseSensor(mac_address)
    sensor.enable_notifications()

    # Wait for heart rate notifications to be received
    try:
        while True:
            if sensor.peripheral.waitForNotifications(.5):
                continue
    except:
        pass
    # Read the battery level and print it
    battery_level = sensor.read_battery_level()
    print("Battery level2: {}%".format(battery_level))

    # Disconnect from the sensor
    sensor.disconnect()
get_heart_rate_and_battery_level()
