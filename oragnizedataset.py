import os
import shutil
from pathlib import Path
from tqdm import tqdm


DATA_DIR = Path("data")
RAW_DIR = DATA_DIR / "plantvillage dataset"   # extracted dataset
IMG_DIR = DATA_DIR / "images"
LBL_DIR = DATA_DIR / "labels"
MASK_DIR = DATA_DIR / "masks"

IMAGES_PER_CLASS = 20   


for d in [IMG_DIR, LBL_DIR, MASK_DIR]:
    d.mkdir(parents=True, exist_ok=True)


classes = []
for path in RAW_DIR.rglob("*"):
    if path.is_dir() and any(path.glob("*.jpg")):
        classes.append(path)


class_names = sorted([c.name for c in classes])
class_to_id = {cls: idx for idx, cls in enumerate(class_names)}


with open(DATA_DIR / "classes.txt", "w") as f:
    for cls in class_names:
        f.write(f"{cls}\n")

print(f"[INFO] Found {len(class_names)} classes")
print(class_to_id)


for cls in tqdm(classes, desc="Processing classes"):
    class_id = class_to_id[cls.name]
    images = list(cls.glob("*.jpg"))[:IMAGES_PER_CLASS]  

    for img_file in images:
        # Copy image to data/images/
        new_img_path = IMG_DIR / f"{cls.name}_{img_file.name}"
        shutil.copy(img_file, new_img_path)

        # Create YOLO label
        lbl_path = LBL_DIR / (new_img_path.stem + ".txt")
        with open(lbl_path, "w") as f:
            f.write(f"{class_id} 0.5 0.5 1.0 1.0\n")

print(f"\n✅ Done! Only {IMAGES_PER_CLASS} images per class copied.")
print("Check: data/images, data/labels, data/classes.txt")
