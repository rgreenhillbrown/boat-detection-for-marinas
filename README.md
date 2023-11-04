# Boat Detection in Marinas

## Introduction
This project aims to develop a robust solution for detecting and counting boats in marinas. Utilising advanced machine learning techniques, specifically the YOLOv8 object detection model, the project includes scripts for detecting boats in YouTube video streams, local video files, and for training the model with custom datasets.

## Contents
- `youtube_detect.py` - Detects boats in video streams from YouTube.
- `local_detect.py` - Detects boats in local video files.
- `train.py` - Trains the YOLO model on a custom dataset for boat detection.

## Installation
### Prerequisites
- Python 3.6 or later
- Pip package manager

### Dependencies
To install the required dependencies, run the following command:
```
pip install ultralytics opencv-python yt-dlp
```

## Usage
### Detecting Boats in YouTube Videos
- **youtube_detect.py**: This script uses YouTube video streams for boat detection.
  - Set up the YouTube URL in the script.
  - Run the script:
    ```
    python youtube_detect.py
    ```

### Detecting Boats in Local Videos
- **local_detect.py**: This script uses local video files for boat detection.
  - Specify the path to your video file in the script.
  - Run the script:
    ```
    python local_detect.py
    ```

### Training the Model
- **train.py**: Train the YOLO model using a custom dataset.
  - Ensure you have the dataset and the configuration files (`yolov8n.yaml` and `boatslocal.yaml`).
  - Run the script:
    ```
    python train.py
    ```

## Contributing
This project is a work in progress.

## License
[MIT License](LICENSE.md)
