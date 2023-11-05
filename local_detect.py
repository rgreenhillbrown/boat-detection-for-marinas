### ref https://www.youtube.com/watch?v=uMzOcCNKr5A
###

from ultralytics import YOLO
import cv2
import os

# load model (yolov8)

model = YOLO('pre-trained.pt')

# load video

video_path = 'path\to\your\video'
cap = cv2.VideoCapture(video_path)

ret = True
# read frames

while ret:
    ret, frame = cap.read()

    # detect and track objects
    results = model.track(frame, persist=True)

    # plot results
    frame_ = results[0].plot()

    # visualise
    cv2.imshow('frame', frame_)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
