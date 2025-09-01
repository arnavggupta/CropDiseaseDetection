from ultralytics import YOLO

def main():
    # Load YOLOv8 nano (very small, fastest)
    model = YOLO("yolov8n.pt")

    # Train
    model.train(
        data="data/data.yaml",
        epochs=2,         # keep very low for your CPU/GPU
        imgsz=256,        # smaller images = faster
        batch=2,          # small batch for low memory
        device="cpu"      # or "0" if you have GPU
    )

if __name__ == "__main__":
    main()
