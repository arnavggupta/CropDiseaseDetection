from ultralytics import YOLO

def evaluate():
    model = YOLO("runs/detect/train2/weights/best.pt")
    metrics = model.val(data="data/data.yaml", imgsz=256, batch=2)
    print(metrics)

if __name__ == "__main__":
    evaluate()
