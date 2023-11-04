from ultralytics import YOLO
#import torch

#torch.cuda.set_device(0)

if __name__ == '__main__':
    # Load model
    model = YOLO("yolov8n.yaml") # model from scratch

    # Use model
    results = model.train(data="boatslocal.yaml", epochs=100, patience=75) # train model