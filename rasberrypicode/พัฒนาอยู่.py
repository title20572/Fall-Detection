import cv2
import numpy as np
import time
import mediapipe as mp
from threading import Timer
from parinya import LINE


file = open('cookie.txt')
name = (r"C:\Users\baben\OneDrive\เดสก์ท็อป\Test\clip\output")
imagename = (r"C:\Users\ADMIN\Desktop\Test\picture")

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
stage = None
create = None
opname = "output.mp4"
img_counter = 0
t = 0
pp = 0

fallminute = 0

line = LINE('pn0zpk8n5TeeQXBrB3N6dw5hs568i6jXmsGmxdC1ID6')

def get_output(out=None):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    if out:
        out.release()
    return cv2.VideoWriter(name + str(time.strftime('%d %m %Y - %H %M %S' )) + '.mp4',fourcc, 15, (640,480))

next_time = time.time() + 900
out = get_output()

def findPosition(image, draw=True):
  lmList = []
  if results.pose_landmarks:
      mp_drawing.draw_landmarks(
         image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
      for id, lm in enumerate(results.pose_landmarks.landmark):
          h, w, c = image.shape
          cx, cy = int(lm.x * w), int(lm.y * h)
          lmList.append([id, cx, cy])
          cv2.circle(image, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
  return lmList

def capture():
  global img_counter
  global t
  global image
  global line
  global fallminute
  
  if t == 0:         
    img_name = imagename + "\opencv_frame.png"
    cv2.imwrite(img_name, image)
    t = 1
    line.sendtext("ผู้สูงอายุล้ม")
    line.sendimage(image)
    fallminute = int(time.strftime('%M'))

  if t == 1:
     sendagain()


def sendagain():
    global pp
    global line
    global fallminute
    minute = int(time.strftime('%M'))
    second = int(time.strftime('%S'))
    # print(fallminute)

    if fallminute % 2 == 0: #เลขคู่
        # print("11")
        if minute % 2 == 0:
          # print("12")
          # print(second)
          if second == 1:
            # print("13")
            if pp == 0:
              pp = 1
              # print("...")
              line.sendtext("fall")
              
          else:
            # print("aaa")
            pp = 0
    else:                   #เลขคี่
        # print("21")
        if minute % 2 == 1:
            # print("22")
            # print(second)
            if second == 1:
              # print("23")
              if pp == 0:
                pp = 1
                # print("...")
                line.sendtext("fall")
                
            else:
              # print("aaa")
              pp = 0


    
    


cap = cv2.VideoCapture(0)

with mp_pose.Pose(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as pose:
  while cap.isOpened():
    success, image = cap.read()
    image = cv2.resize(image, (640,480))
    if not success:
      print("Ignoring empty camera frame.")
      continue
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    lmList = findPosition(image, draw=True)

    if len(lmList) != 0:
      cv2.circle(image, (lmList[12][1], lmList[12][2]), 20, (0, 255, 0), cv2.FILLED)
      cv2.circle(image, (lmList[11][1], lmList[11][2]), 20, (0, 255, 0), cv2.FILLED)
      cv2.circle(image, (lmList[12][1], lmList[12][2]), 20, (0, 255, 0), cv2.FILLED)
      cv2.circle(image, (lmList[11][1], lmList[11][2]), 20, (0, 255, 0), cv2.FILLED)
      

      if (lmList[0][2] >= lmList[12][2]):  #เซไปขวา
        cv2.circle(image, (lmList[12][1], lmList[12][2]), 20, (0, 255, 255), cv2.FILLED)
        cv2.circle(image, (lmList[11][1], lmList[11][2]), 20, (0, 255, 255), cv2.FILLED)
        

        
        
      if (lmList[0][2] >= lmList[11][2]):  #เซไปซ้าย
        cv2.circle(image, (lmList[12][1], lmList[12][2]), 20, (0, 255, 255), cv2.FILLED)
        cv2.circle(image, (lmList[11][1], lmList[11][2]), 20, (0, 255, 255), cv2.FILLED)
        

      if (lmList[0][2] >= lmList[23][2]):  #ล้มทางซ้าย
        cv2.circle(image, (lmList[12][1], lmList[12][2]), 20, (0, 0, 255), cv2.FILLED)
        cv2.circle(image, (lmList[11][1], lmList[11][2]), 20, (0, 0, 255), cv2.FILLED)
        capture()

      if (lmList[0][2] >= lmList[24][2]):  #ล้มทางขวา
        cv2.circle(image, (lmList[12][1], lmList[12][2]), 20, (0, 0, 255), cv2.FILLED)
        cv2.circle(image, (lmList[11][1], lmList[11][2]), 20, (0, 0, 255), cv2.FILLED)
        capture()


      if (lmList[12][2] and lmList[11][2] >= lmList[28][2] and lmList[27][2]):  #คว่ำ
        cv2.circle(image, (lmList[12][1], lmList[12][2]), 20, (0, 0, 255), cv2.FILLED)
        cv2.circle(image, (lmList[11][1], lmList[11][2]), 20, (0, 0, 255), cv2.FILLED)
        capture()

        

    cv2.imshow('Webcam', image)
    if success:
        out.write(image) 

    if time.time() > next_time:
        next_time += 900
        out = get_output(out)



    # if the `q` key was pressed, break from the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # do a bit of cleanup

cv2.destroyAllWindows()