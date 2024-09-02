import cv2

video_cap = cv2.VideoCapture(0)

w = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(video_cap.get(cv2.CAP_PROP_FPS))

video_writer = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*"XVID"), fps, (w,h))
cv2.VideoWriter()

while True:
    ret, frame = video_cap.read()
    
    if not ret:
        break 

    cv2.imshow("video", frame)

    video_writer.write(frame)

    key = cv2.waitKey(1)

    if key == ord("q") or key == ord("Q"):
        break

video_cap.release()
video_writer.release()
