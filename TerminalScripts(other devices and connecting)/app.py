from flask import Flask, request,send_file, render_template, redirect, url_for, send_from_directory
import csv
import time
import os
from datetime import datetime, timedelta
app = Flask(__name__)

message = ""
movement = ""
demand = ""
counting = ""
hr = ""
video_path = '/home/kyle/videos/stretching.mp4'

play_signal_received = False
data_dict = {}
time_threshold_ms = 50
time_threshold = timedelta(milliseconds=time_threshold_ms)
last_timestamps = {}
last_data = {}
def should_combine_data(new_timestamps):
    global last_timestamps
    if last_timestamps is None:
        return False
    for field in last_timestamps:
        if (new_timestamps[field] - last_timestamps[field]) >= time_threshold:
            return False
    return True

@app.route('/message', methods=['GET', 'POST'])
def handle_message():
    global message
    if request.method == 'GET':
        return message
    elif request.method == 'POST':
        message = request.json.get('message', '')
        return 'Message received'

@app.route('/movement', methods=['GET','POST'])
def handle_movement():
    global movement
    if request.method == 'GET':
      return movement
    elif request.method == 'POST':
        movement = request.json.get('movement', '')
        return 'Movement received'

@app.route('/demand', methods=['GET','POST'])
def handle_demand():
    global demand
    if request.method == 'GET':
      return demand
    elif request.method == 'POST':
        demand = request.json.get('demand', '')
        return 'Demand received'

@app.route('/counting', methods=['GET','POST'])
def handle_counting():
    global counting
    if request.method == 'GET':
      return counting
    elif request.method == 'POST':
        counting = request.json.get('counting', '')
        return 'Counting received'

@app.route('/hr', methods=['GET','POST'])
def handle_hr():
    global hr
    if request.method == 'GET':
      return hr
    elif request.method == 'POST':
        hr = request.json.get('hr', '')
        return 'hr received'
#videoplay= False
#@app.route('/video', methods=['GET', 'POST'])
#def serve_video():
    #global videoplay
    #if request.method == 'GET' and request.args.get('signal') == 'play':
        #video_path = '/home/kyle/Desktop/stretching.mp4'  # Replace with the actual path to your video file
        #return send_file(video_path, mimetype='video/mp4')
    #elif request.method == 'POST' and 'signal' in request.form and request.form['signal'] == 'play':
        #return 'Signal received'
    #else:
        #return 'Work'


#@app.route('/video', methods=['GET'])
#def serve_video():
#    global video_path, play_signal_received

         
#    return send_file(video_path, mimetype='video/mp4')

@app.route('/video', methods=['GET'])
def serve_video():
    video_path = 'static/stretching.mp4'  # Path to your video file
    
    return render_template('video.html', video_path=video_path)
    
@app.route('/signal', methods=['POST'])
def receive_signal():
    global play_signal_received

    if 'signal' in request.form and request.form['signal'] == 'play':
        play_signal_received = True

    return 'Signal received'

@app.route('/wait')
def wait():
    global play_signal_received

    while not play_signal_received:
        pass
    play_signal_received = False
    return redirect(url_for('serve_video')) 
    
@app.route('/exercise')
def exercise():
    return render_template('exercise.html')
    
  # Initial filename
def create_new_file():
    global filename

    # Generate a new filename with timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    return f'NAO_{timestamp}.csv'
    
filename = create_new_file()

@app.route('/heart_rate', methods=['POST'])
def receive_heart_rate():
    #global last_timestamps, last_data
    heart_rate = request.form.get('heart_rate')
    speech = request.form.get('speech')
    mov = request.form.get('mov')
    rsangle = request.form.get('rsangle')
    lsangle = request.form.get('lsangle')
    reangle = request.form.get('reangle')
    leangle = request.form.get('leangle')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    
    

    global exist
    # Write heart rate to CSV file
    with open(os.path.join(data_directory, filename), 'a', newline='') as file:
        writer = csv.writer(file)
        headers = ['Timestamp','Heart_rate','Feedback','Movement','Right shoulder angle','Left shoulder angle','Right elbow angle','Left elbow angle']
        if not exist:
          writer.writerow(headers)
          exist = True
        for timestamp, data in data_dict.items():
          writer.writerow([timestamp] + data)
        writer.writerow([timestamp,heart_rate,speech,mov,rsangle,lsangle,reangle,leangle])
        
    return 'Heart rate recorded successfully'

data_directory = 'subject[19]'
exist = False
def setup():
    global filename
    filename = create_new_file()

if __name__ == '__main__':
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
    setup()
    app.run(host='0.0.0.0', port=5000)

