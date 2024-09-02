import cv2

stream = cv2.VideoCapture(0)

while True:
    ret, frame = stream.read()

    if not ret:
        break

    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame = cv2.circle(frame, (frame.shape[0]//2, frame.shape[1]//2), 50, (255,0,0), 3, lineType=cv2.LINE_AA)
    cv2.imshow("Video", frame)
    
    cv2.waitKey(1)

    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows() 