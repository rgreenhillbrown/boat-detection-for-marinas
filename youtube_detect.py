from ultralytics import YOLO
import cv2
import os
import yt_dlp as ydlp

def grab_stream_url(youtube_url):
    ydl_opts = {
        'format': 'best[ext=mp4]',  # Choose the best quality format that is in mp4
    }

    with ydlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False) 
        return info_dict['url']

# Load model (yolov8)
model = YOLO('pre-trained.pt')

# Fetch the video stream URL from YouTube. Uncomment and replace the urls provided to test what it does. You can also try your own. 
youtube_url = 'https://www.youtube.com/watch?v=_sOQkz1xgKc&t=6s' #"https://www.youtube.com/watch?v=ZFsDS0L8Qdk" #https://www.youtube.com/watch?v=_sOQkz1xgKc"
video_stream_url = grab_stream_url(youtube_url)

# Open the video stream using the fetched URL
cap = cv2.VideoCapture(video_stream_url)

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
