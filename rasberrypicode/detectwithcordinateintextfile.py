import cv2
import mediapipe as mp
import datetime as dt


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
stage = None
create = None
txtcount = 1
txtfile = []
rectx = []
recty = []
startPoint = False
endPoint = False
xx1 = 0
xx2 = 0
yy1 = 0
yy2 = 0
ck = 1
fii = 0

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


txtfile = []
x = []
y = []
txtcount = 1
name = 1
cc = 1
t = dt.datetime.now()

cap = cv2.VideoCapture(0)

waitTime = 50



with mp_pose.Pose(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as pose:
  while cap.isOpened():
    if(cc==1):
        with open(str(name) + '.txt','r') as f:
            for line in f:
                cordinate = line.strip().split(',')
                print(cordinate)
                txtfile.append(cordinate)
            for i in cordinate:
                if txtcount % 2 == 1:
                    x.append(i)
                    txtcount = txtcount + 1
            
                else:
                    y.append(i)
                    txtcount = txtcount + 1
        rectx = [int(i) for i in x]
        recty = [int(i) for i in y]
        print(rectx)
        print(recty)
        name = name+1
        cc = cc+1

    delta = dt.datetime.now()-t
    if delta.seconds >= 5:
        rectx.clear()
        recty.clear()
        x.clear()
        y.clear()
        xx1 = 0
        xx2 = 0
        yy1 = 0
        yy2 = 0
        print("clear")
        print(rectx)
        print(recty)
        with open(str(name) + '.txt','r') as f:
            for line in f:
                cordinate = line.strip().split(',')
                txtfile.append(cordinate)
            for i in cordinate:
                if txtcount % 2 == 1:
                    x.append(i)
                    txtcount = txtcount + 1
            
                else:
                    y.append(i)
                    txtcount = txtcount + 1
        rectx = [int(i) for i in x]
        recty = [int(i) for i in y]
        print(rectx)
        print(recty)

        if name == 3:
            name = 1
            print("setname")
        else:
            name = name+1
        t = dt.datetime.now()
    cli = len(rectx)

    success, image = cap.read()
    image = cv2.resize(image, (640,480))
    if not success:
      print("Ignoring empty camera frame.")
      continue
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    lmList = findPosition(image, draw=True)
    cv2.namedWindow('Webcam')
    
    if ck == 1:
        for i in range(cli):
            if i == 0:
                cv2.line(image, (rectx[i], recty[i]), (rectx[i+1], recty[i+1]), (0, 255, 0), 2)
            if i >= 1:
                if i == cli-1:
                    cv2.line(image, (rectx[(cli-1)], recty[(cli-1)]), (rectx[0], recty[0]), (0, 255, 0), 2)
                else:
                    cv2.line(image, (rectx[i], recty[i]), (rectx[i+1], recty[i+1]), (0, 255, 0), 2)

                    

        x1 = min(rectx)
        x2 = max(rectx)
        y1 = min(recty)
        y2 = max(recty)
        xx1 = x1/640
        xx2 = x2/640
        yy1 = y1/480
        yy2 = y2/480
            
            
            

    try:
          landmarks = results.pose_landmarks.landmark
          hhh = (landmarks[mp_pose.PoseLandmark.NOSE.value].x)
          lll = (landmarks[mp_pose.PoseLandmark.NOSE.value].y)
          kkk = str("%.2f"%landmarks[mp_pose.PoseLandmark.NOSE.value].x)
          mmm = str("%.2f"%landmarks[mp_pose.PoseLandmark.NOSE.value].y)
    except:
          pass


    if len(lmList) != 0:
      cv2.circle(image, (lmList[12][1], lmList[12][2]), 20, (0, 255, 0), cv2.FILLED)
      cv2.circle(image, (lmList[11][1], lmList[11][2]), 20, (0, 255, 0), cv2.FILLED)
      cv2.circle(image, (lmList[12][1], lmList[12][2]), 20, (0, 255, 0), cv2.FILLED)
      cv2.circle(image, (lmList[11][1], lmList[11][2]), 20, (0, 255, 0), cv2.FILLED)
      cv2.putText(image, kkk + mmm, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 0), 2)
      


      if (hhh >= xx1 and lll <= yy2 and hhh <= xx2 and lll >= yy1):  #เซไปขวา
        cv2.circle(image, (lmList[12][1], lmList[12][2]), 20, (0, 0, 255), cv2.FILLED)
        cv2.circle(image, (lmList[11][1], lmList[11][2]), 20, (0, 0, 255), cv2.FILLED)
        
        
    cv2.resizeWindow("Webcam", 640, 480)
    cv2.imshow('Webcam', image)
    


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()