import cv2
num=0
videoWebcam = cv2.VideoCapture("http://192.168.0.109:81/videostream.cgi?user=Poloisirs&pwd=1203")
#videoWebcam = cv2.VideoCapture(0)
face_model = cv2.CascadeClassifier("stop_data.xml")
while True:
    
    valeurRetour, imageWebcam = videoWebcam.read()
    gray = imageWebcam
    #gray = cv2.cvtColor(imageWebcam, cv2.COLOR_BGR2GRAY)
    faces = face_model.detectMultiScale(gray)
    visage=False
    for face in faces:
        cv2.rectangle(gray, (face[0], face[1]), (face[0] + face[2], face[0] + face[3]), (255, 0, 0), 3)
        out = cv2.imwrite('pan/%s.png' % (num), imageWebcam)
        num=num+1
        visage=True
    cv2.imshow('Image de la webcam', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
videoWebcam.release()
cv2.destroyAllWindows() 
print(num)
