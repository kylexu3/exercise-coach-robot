def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle
def read_hr():
    response = requests.get(hr_url)
    hr = response.text.strip()
        
    return hr
    
def send_movement(movement):
    data = {'movement': movement}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(movement_url, json=data, headers=headers)
def send_mov(mov):
    data = {'mov': mov}

    response = requests.post(heart_rate_url, data=data)
def send_rsangle(rsangle):     
	# Send heart rate to the Flask server
	
	data = {'rsangle': rsangle}
	response = requests.post(heart_rate_url, data=data)
def send_lsangle(lsangle):     
	# Send heart rate to the Flask server
	
	data = {'lsangle': lsangle}
	response = requests.post(heart_rate_url, data=data)
def send_reangle(reangle):     
	# Send heart rate to the Flask server
	
	data = {'reangle': reangle}
	response = requests.post(heart_rate_url, data=data)
def send_leangle(leangle):     
	# Send heart rate to the Flask server
	
	data = {'leangle': leangle}
	response = requests.post(heart_rate_url, data=data)
def send_counting(counting):
    data = {'counting': counting}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(counting_url, json=data, headers=headers)
    return True
def read_demand():
    # Read the movement from the online source
    response = requests.get(demand_url)
    demand = response.text.strip()
    return demand

def has_increasing_tendency(angle_list):
    increasing_count = 0
    for i in range(1, len(angle_list)):
        if angle_list[i] > angle_list[i-1] or angle_list[i] > angle_list[i-2] or angle_list[i] > angle_list[i-4]:
            increasing_count += 1
    return increasing_count >= len(angle_list) * 0.5

def has_decreasing_tendency(angle_list):
    decreasing_count = 0
    for i in range(1, len(angle_list)):
        if angle_list[i]  < angle_list[i-1] or angle_list[i] < angle_list[i-2] or angle_list[i] < angle_list[i-4] :
            decreasing_count += 1
    return decreasing_count >= len(angle_list) * 0.5
    
def draw_data(image, x, counter, stage):
    # Draw status box
    cv2.rectangle(image, (x, 0), (x + 250, 73), (245, 117, 16), -1)

    # Draw "REPS" text
    cv2.putText(image, 'REPS', (x + 15, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    # Draw counter value
    cv2.putText(image, str(counter), (x + 10, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

    # Draw "STAGE" text
    cv2.putText(image, 'STAGE', (x + 85, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    # Draw stage value
    cv2.putText(image, stage, (x + 85, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
def draw_data2(image,counter, stage):
    cv2.rectangle(image, (0,0), (250,73), (245,117,16), -1)
        
        #Rep data 
    cv2.putText(image, 'REPS', (15,12),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
			
    cv2.putText(image, str(counter), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
			
			
        #Stage data 
    cv2.putText(image, 'STAGE', (95,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
			
    cv2.putText(image, stage, (95,60),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)	
def draw_data3(image, heart_rate):
    cv2.rectangle(image, (0, image.shape[0] -80), (270, image.shape[0]), (245, 117, 16), -1)

    # Heart rate data
    cv2.putText(image, 'HEART RATE', (15, image.shape[0] - 61), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(image, str(heart_rate), (10, image.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(image, 'bmp', (130, image.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
def draw_landmark():
        mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS, 
                                 mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                                 mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
                                 )
        
        # 2. Right hand
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4),
                                 mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                                 )

        # 3. Left Hand
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                                 mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                                 )

        # 4. Pose Detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                 )
import cv2
import mediapipe as mp
import numpy as np
import requests
import time
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
movement_url = 'http://192.168.1.134:5000/movement'
demand_url = 'http://192.168.1.134:5000/demand'
counting_url = 'http://192.168.1.134:5000/counting'
heart_rate_url ='http://192.168.1.134:5000/heart_rate'
hr_url ='http://192.168.1.134:5000/hr'
t0 = time.time()
t01 = time.time()
cap = cv2.VideoCapture(2)
# Initiate holistic model'
#setup mediapipe instance 
counter = 0
stage = None
state = None
countlu = 0
countru = 0
countld = 0
countrd = 0
countleu = 0
countreu = 0
countled = 0
countb = 0
counter2 = 0
counts = 0
test = 1
total = 0
stage2 = None
sync = 0
sync1 = 0
activate = 0
angle_list_left = [] 
angle_list_right = [] 
angle_list_lelbow = [] 
movement = 'None'
send_movement(movement)
width = 1000
length = 800
output_size = (width, length)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    

 while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.resize(frame, output_size)
        # Recolor image
        # Recolor Feed
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Make Detections
        results = holistic.process(image)
        # print(results.face_landmarks)
        
        # face_landmarks, pose_landmarks, left_hand_landmarks, right_hand_landmarks
        
        # Recolor image back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        
        try:
            landmarks = results.pose_landmarks.landmark
            
            #Left_Hand
            # Get coordinates
            L_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            L_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            L_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            
            # Calculate angle
            L_elbow_angle = int (calculate_angle(L_shoulder, L_elbow, L_wrist))
            
            # Visualize angle
            cv2.putText(image, str(L_elbow_angle), 
                           tuple(np.multiply(L_elbow, output_size).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )
                   
            
            #Right_Hand
            # Get coordinates
            R_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            R_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            R_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
            # Calculate angle
            R__elbow_angle = int (calculate_angle(R_shoulder, R_elbow, R_wrist))
            
            # Visualize angle
            cv2.putText(image, str(R__elbow_angle), 
                           tuple(np.multiply(R_elbow, output_size).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )        
                                
               
                                
                                
                                
                                
                                
            #Left_Hand
            # Get coordinates
            L_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            L_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            L_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            
            
            # Calculate angle
            L_shoulder_angle = int (calculate_angle(L_hip, L_shoulder,L_elbow))
            
            
            
            # Visualize angle
            cv2.putText(image, str(L_shoulder_angle), 
                           tuple(np.multiply(L_shoulder, output_size).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )
            
            #Right_Hand
            # Get coordinates
            R_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]           
            R_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            R_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            
# Calculate the position coordinates relative to the new width and height
           
            
            # Calculate angle
            R_shoulder_angle = int (calculate_angle(R_hip, R_shoulder, R_elbow))
            
            cv2.putText(image, str(R_shoulder_angle), 
                           tuple(np.multiply(R_shoulder, output_size).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                ) 
            #Right_neck
            # Get coordinates
            L_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]           
            R_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            Nose = [landmarks[mp_pose.PoseLandmark.NOSE.value].x,landmarks[mp_pose.PoseLandmark.NOSE.value].y]
            R_eye = [landmarks[mp_pose.PoseLandmark.RIGHT_EYE_OUTER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_EYE_OUTER.value].y]
                        
            # Calculate angle
            R_angle = int (calculate_angle(L_shoulder, R_shoulder, Nose))
            
            # Visualize angle
            cv2.putText(image, str(R_angle), 
                           tuple(np.multiply(R_eye, output_size).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )  	                    
                                                                       
             #Left_neck
            # Get coordinates
            L_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]           
            R_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            Nose = [landmarks[mp_pose.PoseLandmark.NOSE.value].x,landmarks[mp_pose.PoseLandmark.NOSE.value].y]
            L_eye = [landmarks[mp_pose.PoseLandmark.LEFT_EYE_OUTER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_EYE_OUTER.value].y]
                        
            # Calculate angle
            L_angle = int (calculate_angle( R_shoulder, L_shoulder, Nose))
            
            # Visualize angle
            cv2.putText(image, str(L_angle), 
                           tuple(np.multiply(L_eye, output_size).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )       
            demand=read_demand()
            #demand = "Activatebf"
            #BASIC MARCHING
            if demand== "Activatebm" :
              angle_list_left.append(L_shoulder_angle)
              t1 = time.time()
              if has_increasing_tendency(angle_list_left) and L_shoulder_angle>20:  
                if max(angle_list_left) < 70:
                  countlu+= 1
                  if countlu >= 20:
                    movement = 'Raisel'
                    send_movement(movement)
                    mov = movement
                    send_mov(mov)
                    print(movement)
                    angle_list_left = [] 
                    t0=time.time()
                    countlu = 0
                    countld = 0
                elif max(angle_list_left)>=70 and max(angle_list_left)<150:
                    movement = 'Right movement'
                    send_movement(movement)
                    mov = movement
                    send_mov(mov)
                    t0=time.time()
                    print(movement)
                    angle_list_left = []
                    countlu =0
                    #countld =0
                elif L_shoulder_angle >= 150:
                    movement = 'Downl'
                    send_movement(movement)
                    mov = movement
                    send_mov(mov)
                    t0=time.time()
                    angle_list_left = [] 
                    print(movement)
                    countlu = 0
                    #countld = 0
              elif has_decreasing_tendency(angle_list_left):
                  if min(angle_list_left)>20:
                    countld+=1
                    if countld >= 20:
                      movement = 'Backl'
                      send_movement(movement)
                      mov = movement
                      send_mov(mov)
                      t0=time.time()
                      print(movement)
                      angle_list_left = []
                      countld =0
                      conutlu = 0
                  else: 
                      angle_list_left = []
                      countld =0
                      countlu = 0
                  #elif min(angle_list_left)<=20:
                      #movement = 'Right movement'
                      #send_movement(movement)
                      #t0=time.time()
                      #print(movement)
                      #angle_list_left = []
                      #countld = 0
              else:
                  t1 = time.time()             
                  if t1-t0>=1:
                    angle_list_right = []
                    angle_list_left = []
                    countrd = 0
                    countru = 0
                    print("new")
                    t0= time.time()
########################################################### SINGLE ARM FOLD      
            if demand== "Activatesf" :
              angle_list_left.append(L_shoulder_angle)
              #t1=time.time()
              
              if has_increasing_tendency(angle_list_left) and L_shoulder_angle>30: 
                
                if max(angle_list_left) < 80:
                  countlu+= 1
                  if countlu >= 10:
                    movement = 'Raiself'
                    send_movement(movement)
                    mov = movement
                    send_mov(mov)
                    print(movement)
                    angle_list_left = []
                    angle_list_lelbow = [] 
                    t0=time.time()
                    countlu = 0
                    countld = 0
                elif max(angle_list_left)>=70 and max(angle_list_left)<130 and L_elbow_angle<=45:
                    sync =1
                    t0=time.time()
                    angle_list_left = []
                    angle_list_lelbow = []
                    countlu =0
                    countleu = 0
                    #countld =0
                elif max(angle_list_left)>=70 and max(angle_list_left)<130 and L_elbow_angle>45:   
                    countleu +=1
                    if countleu >=10:
                      movement = 'Foldl'
                      send_movement(movement)
                      mov = movement
                      send_mov(mov)
                      print(movement)
                      angle_list_left = [] 
                      angle_list_lelbow = []
                      t0=time.time()
                      countlu = 0
                      #countld = 0
                      countleu = 0
                elif L_shoulder_angle >= 130:
                    movement = 'Downl'
                    send_movement(movement)
                    mov = movement
                    send_mov(mov)
                    t0=time.time()
                    angle_list_left = [] 
                    print(movement)
                    countlu = 0
                    countleu = 0
                    #countld = 0
              elif has_decreasing_tendency(angle_list_left):
                  if min(angle_list_left)>20:
                    countld+=1
                    #sync1 = 0
                    if countld >= 15:
                      movement = 'Backl'
                      send_movement(movement)
                      mov = movement
                      send_mov(mov)
                      t0=time.time()
                      print(movement)
                      angle_list_left = []
                      countld =0
                      sync1 = 0
                      #conutlu = 0
                  else: 
                      angle_list_left = []
                      countld =0
                      sync1 = 0
                      #countlu = 0
                  #elif min(angle_list_left)<=20:
                      #movement = 'Right movement'
                      #send_movement(movement)
                      #t0=time.time()
                      #print(movement)
                      #angle_list_left = []
                      #countld = 0
              #else:
                  #t1 = time.time()             
                  #if t1-t0>=1:
                    #angle_list_right = []
                    #angle_list_left = []
                    #countrd = 0
                    #countru = 0
                    #t0= time.time()                    
            if demand == "Activatesf" or demand == "Activatebf" or demand== "Activateba":        
              if L_angle <50 and R_angle <50 :
                movement="Neck"
                #send_movement(movement)
                #print ("Neck")  
            if demand== "Activatebm" :
              angle_list_right.append(R_shoulder_angle)
              t1 = time.time()
              if has_increasing_tendency(angle_list_right) and R_shoulder_angle>20:  
                if max(angle_list_right) < 70:
                  countru+= 1
                  if countru >= 20:
                    movement = 'Raiser'
                    send_movement(movement)
                    print(movement)
                    mov = movement
                    send_mov(mov)
                    angle_list_right = [] 
                    t0=time.time()
                    countru = 0
                    countrd = 0
                elif max(angle_list_right)>=70 and max(angle_list_right)<150:
                    movement = 'Right movement'
                    send_movement(movement)
                    mov = movement
                    send_mov(mov)
                    t0=time.time()
                    print(movement)
                    angle_list_right = []
                    countru =0
                    #countrd =0
                elif R_shoulder_angle >= 150:
                    movement = 'Downr'
                    send_movement(movement)
                    mov = movement
                    send_mov(mov)
                    t0=time.time()
                    angle_list_right = [] 
                    print(movement)
                    countru = 0
                    #countrd = 0
              elif has_decreasing_tendency(angle_list_right):
                  print("decrease")
                  if min(angle_list_right)>20:
                    countrd+=1
                    if countrd >= 20:
                      movement = 'Backr'
                      send_movement(movement)
                      mov = movement
                      send_mov(mov)
                      t0=time.time()
                      print(movement)
                      angle_list_right = []
                      countrd =0
                      conutru = 0
                  else: 
                      angle_list_right = []
                      countrd =0
                      countru = 0
                  #elif min(angle_list_right)<=20:
                      #movement = 'Right movement'
                      #send_movement(movement)
                      #t0=time.time()
                      #print(movement)
                      #angle_list_right = []
                      #countrd = 0
              else:
                  t11 = time.time()             
                  if t11-t01>=1:
                    angle_list_right = []
                    angle_list_left = []
                    countrd = 0
                    countru = 0
                    print("new")
                    t01= time.time()
##################################################SINGLE ARM FOLD
            if demand== "Activatesf" :
              angle_list_right.append(R_shoulder_angle)
              rsangle = R_shoulder_angle
              send_rsangle(rsangle)
              lsangle = L_shoulder_angle
              send_lsangle(lsangle)
              reangle = R__elbow_angle
              send_reangle(reangle)
              leangle = L_elbow_angle
              send_leangle(leangle)
              if (has_increasing_tendency(angle_list_right) and R_shoulder_angle>30) and (has_increasing_tendency(angle_list_left) and L_shoulder_angle>30):
                countb += 1
                if countb >= 5:
                  movement = "Notboth"
                  send_movement (movement)
                  sync1 = 1
                  mov = movement
                  send_mov(mov)
                  countru = 0
                  countru = 0
                  countlu = 0
                  print(movement)
                  countb = 0
              elif has_increasing_tendency(angle_list_right) and R_shoulder_angle>30:  
                if max(angle_list_right) < 80:
                  countru+= 1
                  if countru >= 10:
                    movement = 'Raiserf'
                    send_movement(movement)
                    mov = movement
                    send_mov(mov)
                    print(movement)
                    angle_list_right = []
                    angle_list_lelbow = [] 
                    t0=time.time()
                    countru = 0
                    countrd = 0
                elif max(angle_list_right)>=70 and max(angle_list_right)<130 and R__elbow_angle<=45 and sync == 1 and sync1 == 0:
                    movement = 'Right movement'
                    send_movement(movement)
                    mov = movement
                    send_mov(mov)
                    t0=time.time()
                    print(movement)
                    angle_list_right = []
                    angle_list_lelbow = []
                    countru =0
                    countreu = 0
                    sync = 0
                    #countrd =0
                elif max(angle_list_right)>=70 and max(angle_list_right)<130 and R__elbow_angle>45:   
                    countreu +=1
                    if countreu >=10:
                      movement = 'Foldr'
                      send_movement(movement)
                      mov = movement
                      send_mov(mov)
                      print(movement)
                      angle_list_right = [] 
                      angle_list_lelbow = []
                      t0=time.time()
                      countru = 0
                      countrd = 0
                      countreu = 0
                elif R_shoulder_angle >= 130:
                    movement = 'Downr'
                    send_movement(movement)
                    mov = movement
                    send_mov(mov)
                    t0=time.time()
                    angle_list_right = [] 
                    print(movement)
                    countru = 0
                    countreu = 0
                    #countrd = 0
              elif has_decreasing_tendency(angle_list_right):
                  if min(angle_list_right)>20:
                    countrd+=1
                    #sync1 = 0
                    if countrd >= 15:
                      movement = 'Backr'
                      send_movement(movement)
                      mov = movement
                      send_mov(mov)
                      t0=time.time()
                      print(movement)
                      sync1 = 0
                      angle_list_right = []
                      countrd =0
                      #countru = 0
                  else: 
                      angle_list_right = []
                      countrd =0
                      sync1 = 0
                      #countru = 0
                  #elif min(angle_list_right)<=20:
                      #movement = 'Right movement'
                      #send_movement(movement)
                      #t0=time.time()
                      #print(movement)
                      #angle_list_right = []
                      #countrd = 0
              else:
                  t11 = time.time()             
                  if t11-t01>=1:
                    angle_list_right = []
                    angle_list_left = []
                    #countrd = 0
                    #countru = 0
                    print("new")
                    t01= time.time()
########################################################### BOTH ARM FOWARD
            if demand== "Activatest" :
              angle_list_right.append(R_shoulder_angle)
              angle_list_left.append(L_shoulder_angle)
              
              if ((has_increasing_tendency(angle_list_right) and R_shoulder_angle>30) and (has_increasing_tendency(angle_list_left) and L_shoulder_angle>30)) :   
                #t1 = time.time()
                #print("increase")
                if max(angle_list_right) < 160 or max(angle_list_left) < 160 :
                  countru+= 1
                  if countru >= 20:
                    movement = 'Raiseb'
                    send_movement(movement)
                    print(movement)
                    angle_list_right = [] 
                    angle_list_left=[]
                    t0=time.time()
                    countru = 0
                    countrd = 0
                    countlu = 0
                    countld = 0
                elif max(angle_list_right)>=160 and max(angle_list_left)>=160:
                    countld+= 1
                    if countld >= 20:
                      movement = 'Right movement'
                      send_movement(movement)
                      t0=time.time()
                      print(movement)
                      angle_list_right = []
                      angle_list_left=[]
                      countru =0
                      countlu = 0
                      countrd =0
                      countld = 0
              else:
                  t1 = time.time()             
                  if t1-t0>=1:
                    angle_list_right = []
                    angle_list_left = []
                    #countrd = 0
                    #countru = 0
                    print("new")
                    t0= time.time() 
############################################################################                   
            if demand== "Activateba" :
              angle_list_right.append(R_shoulder_angle)
              angle_list_left.append(L_shoulder_angle)
              rsangle = R_shoulder_angle
              send_rsangle(rsangle)
              lsangle = L_shoulder_angle
              send_lsangle(lsangle)
              reangle = R__elbow_angle
              send_reangle(reangle)
              leangle = L_elbow_angle
              send_leangle(leangle)
              if ((has_increasing_tendency(angle_list_right) and R_shoulder_angle>30) and (has_increasing_tendency(angle_list_left) and L_shoulder_angle>30)) :   
                #t1 = time.time()
                print("increase")
                if max(angle_list_right) < 160 or max(angle_list_left) < 160 :
                  countru+= 1
                  if countru >= 20:
                    movement = 'Raiseb'
                    send_movement(movement)
                    mov = movement
                    send_mov(mov)
                    print(movement)
                    angle_list_right = [] 
                    angle_list_left=[]
                    t0=time.time()
                    countru = 0
                    #countrd = 0
                    countlu = 0
                    countld = 0
                elif max(angle_list_right)>=160 and max(angle_list_left)>=160 and R__elbow_angle >=150 and L_elbow_angle >=150:
                    countld+= 1
                    if countld >= 10:
                      movement = 'Right movement'
                      send_movement(movement)
                      mov = movement
                      send_mov(mov)
                      t0=time.time()
                      print(movement)
                      angle_list_right = []
                      angle_list_left=[]
                      countru =0
                      countlu = 0
                      #countrd =0
                      countld = 0
                elif R__elbow_angle <150 or L_elbow_angle <150:
                    countlu+= 1
                    if countlu >= 10:
                      movement = 'Extend'
                      send_movement(movement)
                      mov = movement
                      send_mov(mov)
                      print(movement)
                      t0=time.time()
                      angle_list_right = []
                      angle_list_left=[]
                      countlu = 0
                      countru =0
                      #countrd =0
                      countld = 0
              elif has_decreasing_tendency(angle_list_right) and has_decreasing_tendency(angle_list_left) :            
                  if min(angle_list_right)>20 or min(angle_list_left)>20:
                    countrd+=1
                    if countrd >= 20:
                      movement = 'Backb'
                      send_movement(movement)
                      mov = movement
                      send_mov(mov)
                      t0=time.time()
                      print(movement)
                      angle_list_right = []
                      angle_list_left = []
                      countrd =0
                      conutru = 0
                  else: 
                      angle_list_left = []
                      angle_list_right = []
                      countrd =0
                      #countru = 0
                  #elif min(angle_list_right)<=20:
                      #movement = 'Right movement'
                      #send_movement(movement)
                      #t0=time.time()
                      #print(movement)
                      #angle_list_right = []
                      #countrd = 0
              else:
                  t1 = time.time()             
                  if t1-t0>=1:
                    angle_list_right = []
                    angle_list_left = []
                    #countrd = 0
                    #countru = 0
                    print("new")
                    t0= time.time()
              
################################################################### BOTH ARM FOLD
            if demand== "Activatebf" :
              angle_list_right.append(R_shoulder_angle)
              angle_list_left.append(L_shoulder_angle)
              
              rsangle = R_shoulder_angle
              send_rsangle(rsangle)
              lsangle = L_shoulder_angle
              send_lsangle(lsangle)
              reangle = R__elbow_angle
              send_reangle(reangle)
              leangle = L_elbow_angle
              send_leangle(leangle)
              t1 = time.time()
              if (has_increasing_tendency(angle_list_right) and R_shoulder_angle>30) and (has_increasing_tendency(angle_list_left) and L_shoulder_angle>30) :  
                if max(angle_list_right) < 70 or max(angle_list_left) < 70 :
                  countru+= 1
                  if countru >= 15:
                    movement = 'Raisebf'
                    send_movement(movement)
                    mov = movement
                    send_mov(mov)
                    print(movement)
                    angle_list_right = [] 
                    angle_list_left=[]
                    t0=time.time()
                    countru = 0
                    #countrd = 0
                    countlu = 0
                    countld = 0
                elif max(angle_list_right)>=70 and max(angle_list_left)>=70 and R__elbow_angle <=45 and L_elbow_angle <=45 and max(angle_list_right)<=130 and max(angle_list_left)<=130:
                    countld+= 1
                    if countld >= 5:
                      movement = 'Right movement'
                      send_movement(movement)
                      mov = movement
                      send_mov(mov)
                      t0=time.time()
                      print(movement)
                      angle_list_right = []
                      angle_list_left=[]
                      countru =0
                      countlu = 0
                      #countrd =0
                      countld = 0
                elif (max(angle_list_left)>=70 and max(angle_list_left)<130 and L_elbow_angle>45) or (max(angle_list_right)>=70 and max(angle_list_right)<130 and R__elbow_angle>45):
                    countlu+= 1
                    if countlu >= 10:
                      movement = 'Foldb'
                      send_movement(movement)
                      mov = movement
                      send_mov(mov)
                      print(movement)
                      t0=time.time()
                      countlu = 0
                      #countrd =0
                      countld = 0
                      angle_list_right = []
                      angle_list_left=[]
                elif max(angle_list_left)>=130 or max(angle_list_right)>=130:
                    movement = 'Downb'
                    send_movement(movement)
                    mov = movement
                    send_mov(mov)
                    print(movement)
                    t0=time.time()
                    countlu = 0
                    countrd =0
                    countld = 0
                    angle_list_right = []
                    angle_list_left=[]
              elif has_decreasing_tendency(angle_list_right) and has_decreasing_tendency(angle_list_left) :
                  if min(angle_list_right)>20 or min(angle_list_left)>20:
                    countrd+=1
                    if countrd >= 15:
                      movement = 'Backb'
                      send_movement(movement)
                      mov = movement
                      send_mov(mov)
                      t0=time.time()
                      print(movement)

                      angle_list_right = []
                      angle_list_left = []
                      countrd =0
                      conutru = 0
                  else: 
                      angle_list_left = []
                      angle_list_right = []
                      countrd =0
                      #countru = 0
                  #elif min(angle_list_right)<=20:
                      #movement = 'Right movement'
                      #send_movement(movement)
                      #t0=time.time()
                      #print(movement)
                      #angle_list_right = []
                      #countrd = 0
              else:
                  t1 = time.time()             
                  if t1-t0>=1:
                    angle_list_right = []
                    angle_list_left = []
                    #countrd = 0
                    #countru = 0
                    print("new")
                    t0= time.time()
            
             
#####################################################  BM  COUNT
            
            if demand== "Activatebm":
            # Right Curl counter logic
              if  L_shoulder_angle > 70:
                 stage2 = "down"
              if  L_shoulder_angle < 20 and stage2 == 'down':
                 stage2 = "up"
                 counter2 += 1
                 print ("L_arm = ", counter2)
              #Left Curl counter logic
              if  R_shoulder_angle > 70:
                 stage = "down"
              if  R_shoulder_angle < 20 and stage == 'down':
                 stage= "up"
                 counter += 1
                 print ("R_arm = ", counter)
            if demand == "Deactivatebm":
              total = (counter + counter2)//2
              counting =str(total)
              send_counting(counting)
   
#####################################################   Single arm fold count
            if demand == "Activatesf" or (demand == "Presf" and counts ==1):
            # Right Curl counter logic
             if  R_shoulder_angle > 70 and  R__elbow_angle < 45  :
               stage = "down"
               
               if demand == "Presf" and R_shoulder_angle >= 130 :
                 movement = "Upcorrectdr"
                 send_movement(movement)
                 stage = "up"
                 print (movement)
               elif demand == "Presf":
                 movement = "Upcorrectr"
                 send_movement(movement)
                 stage = "down"
                 print (movement)
             elif demand == "Presf" and R_shoulder_angle > 70 and R_shoulder_angle <130 and R__elbow_angle>=45:
               movement = "Upfoldr"
               send_movement(movement)
               #stage = "up"
               print (movement)
               
             if  R_shoulder_angle < 20 and  R__elbow_angle > 150  and  stage == 'down':
               stage = "up"
               counter += 1
               print ("R_Hand= ", counter)
               if demand == "Presf":
                 movement = "Downcorrectr"
                 send_movement(movement)
                 counts += 1
                 
                 print (movement)
             elif demand == "Presf" and R_shoulder_angle < 20 and  R__elbow_angle <= 150 and stage =='down':
               movement = "Downstretchr"
               send_movement(movement)
               print (movement)
               
            # Left Curl counter logic
             if  L_shoulder_angle > 70 and L_elbow_angle < 45 :
               stage2 = "down"
               if demand == "Presf":
                 movement = "Upcorrectl"
                 send_movement(movement)
                 stage2 = "down"
                 print (movement)
               elif demand == "Presf" and L_shoulder_angle >= 130 :
                 movement = "Upcorrectdl"
                 send_movement(movement)
                 stage = "up"
                 print (movement)
             elif demand == "Presf" and L_shoulder_angle > 70 and L_elbow_angle>=45:
               movement = "Upfoldl"
               send_movement(movement)
               #stage = "up"
               print (movement)
               
             if  L_shoulder_angle < 20 and  L_elbow_angle > 150 and stage2 == 'down':
               stage2 = "up"
               counter2 += 1
               print ("L_Hand = ", counter2)
               if demand == "Presf":
                 movement = "Downcorrectl"
                 send_movement(movement)
                 counts += 1
                 print (movement)
             elif demand == "Presf" and L_shoulder_angle < 20 and  L_elbow_angle <= 150 and stage2 == 'down':
                 movement = "Downstretchl"
                 send_movement(movement)
                 print (movement)
               
               
               
             total = (counter + counter2)//2
             counting =str(total)
             send_counting(counting)
           
            if demand == "Deactivatesf":
              total = (counter + counter2)//2
              counting =str(total)
              send_counting(counting)
   
############################################# BOTH ARM FORWARD COUNT
            if demand == "Activateba" or (demand == "Preba" and counts ==2):
             if  R_shoulder_angle > 160 and L_shoulder_angle > 160 and R__elbow_angle > 150  and L_elbow_angle > 150 :
               stage = "down"
               if demand == "Preba":
                 movement = "Upcorrect"
                 send_movement(movement)
                 print (movement)
                 stage = "down"
             elif demand == "Preba" and ( (R_shoulder_angle > 80 and R__elbow_angle <= 150) or (L_shoulder_angle > 80 and L_elbow_angle<= 150)):
               movement = "Upstretch"
               send_movement(movement)
               #stage = "up"
               print (movement)
             if  R_shoulder_angle < 20 and L_shoulder_angle < 20 and R__elbow_angle > 150  and L_elbow_angle > 150 and stage == 'down':
               stage = "up"
               counter += 1
               if demand == "Preba":
                 movement = "Downcorrect"
                 send_movement(movement)
                 stage = "up"
                 counts += 1
                 print (movement)
               total = counter
               counting =str(total)
               send_counting(counting)
               print ("Arm = ", counter)
             elif demand == "Preba" and stage == 'down' and ((R_shoulder_angle < 20 and R__elbow_angle <= 150) or (L_shoulder_angle < 20 and  L_elbow_angle <= 150)) :
               movement = "Downstretch"
               send_movement(movement)
               print (movement)
               total = counter
               #counting =str(total)
               #send_counting(counting)
               print ("Arm = ", counter)
            if demand == "Deactivateba":
              total = (counter + counter2)
              counting =str(total)
              send_counting(counting)
 
################################################### BOTH ARMS FOLD COUNT      
            if demand == "Activatebf" or (demand =="Prebf" and counts == 0):
             if  R_shoulder_angle >= 70 and L_shoulder_angle >= 70 and R__elbow_angle <= 45  and L_elbow_angle <= 45 :
               stage = "down"
               
               if demand == "Prebf" and (R_shoulder_angle >= 130 or L_shoulder_angle>= 130):
                 movement = "Upcorrectd"
                 send_movement(movement)
                 #stage = "up"
                 print (movement)
               elif demand == "Prebf":
                 movement = "Upcorrect"
                 send_movement(movement)
                 print (movement)
                 stage = "down"
             elif demand == "Prebf" and ((R_shoulder_angle> 70 and R__elbow_angle > 45) or (L_shoulder_angle > 70 and L_elbow_angle>45)):
               movement = "Upfold"
               send_movement(movement)
               #stage = "up"
               print (movement)
             if  R_shoulder_angle < 20 and L_shoulder_angle < 20 and R__elbow_angle > 150  and L_elbow_angle > 150 and stage == 'down':
               stage = "up"
               counter += 1
               if demand == "Prebf":
                 movement = "Downcorrect"
                 counts += 1
                 send_movement(movement)
                 stage = "up"
                 print (movement)
               total = counter
               counting =str(total)
               send_counting(counting)
               print ("Arm = ", counter)
             elif demand == "Prebf" and stage == 'down' and ((R_shoulder_angle < 20 and R__elbow_angle <= 150) or (L_shoulder_angle < 20 and  L_elbow_angle <= 150)) :
               movement = "Downstretch"
               send_movement(movement)
               print (movement)
            if demand == "Deactivatebf":
              total = (counter + counter2)
              counting =str(total)
              send_counting(counting)
            if demand == "Decent":
              counts = 1
            if demand == "Decent1":
              counts = 2
            if demand == "Clear":
              total = 0
              counter = 0
              counter2 = 0   
              countlu = 0
              countru = 0
              countld = 0
              countrd = 0
              countleu = 0
              countreu = 0
              countled = 0
              sync = 0
              movement = 'None'
            
              send_movement(movement)
              angle_list_left = [] 
              angle_list_right = [] 
              angle_list_lelbow = []  
              counting = str(total)
              send_counting(counting)
              stage = 'None'
              stage2 = 'None' 
            if demand == "Pause":
              movement = 'None'
              send_movement(movement)
        except:
            pass
            
        #Render curl counter
        #Setup status box
        
        demand = read_demand()
        #demand = "Start"
        #demand = "Activatesf"
        heart_rate = read_hr()
        if demand == "Activatebm" or demand == "Activatesf" or demand == "Presf":
          draw_data(image, 0, counter, stage)     # Draw data for the first counter
          draw_data(image, width-250 , counter2, stage2)
        if demand == "Activateba" or demand == "Activatebf"or demand =="Prebf" or demand == "Preba":
          draw_data2(image, counter, stage) 	
        if demand != "Activateba" and demand != "Activatebf"and demand !="Prebf" and demand != "Preba" and demand != "Activatesf" and demand != "Deactivateba" and demand != "Deactivatebf" and demand != "Deactivatesf" and demand != "Clear" and demand != "Pause" and demand != "Start" and demand != "Prebf" and demand != "Presf" and demand != "Preba" and demand != "Decent" and demand != "Decent1":
          cv2.rectangle(image, (0, 0), (output_size), (245, 117, 16), -1)
          
        #draw_data3(image, heart_rate)
        #print(str(heart_rate))
        # 1. Draw face landmarks
        if demand == "Start":
          activate = 1
        if activate == 1:
          draw_landmark()
          draw_data3(image, heart_rate)
        cv2.imshow('Raw Webcam Feed', image)
        
        #show coordinates
        #print (results.left_hand_landmarks)
        #print (results.right_hand_landmarks)
        #print (L_hib)
        #print (landmarks)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
