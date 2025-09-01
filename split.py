# split_dataset.py
import random
from pathlib import Path
import shutil

random.seed(42)

SRC_IMG = Path("data/images")
SRC_LBL = Path("data/labels")
OUT_IMG = Path("data/images_split")
OUT_LBL = Path("data/labels_split")

for p in [OUT_IMG / "train", OUT_IMG / "val", OUT_LBL / "train", OUT_LBL / "val"]:
    p.mkdir(parents=True, exist_ok=True)

# collect mapping from class_id -> list of stems
class_map = {}
for lbl in SRC_LBL.glob("*.txt"):
    stem = lbl.stem
    txt = lbl.read_text().strip().splitlines()
    if not txt:
        continue
    cls = int(txt[0].split()[0])
    class_map.setdefault(cls, []).append(stem)

train_ratio = 0.8

for cls, stems in class_map.items():
    random.shuffle(stems)
    split = int(len(stems) * train_ratio)
    train = stems[:split]
    val = stems[split:]
    for s in train:
        # find image file with any extension
        for ext in [".jpg", ".jpeg", ".png", ".JPG", ".PNG"]:
            src_img = SRC_IMG / (s + ext)
            if src_img.exists():
                shutil.copy2(src_img, OUT_IMG / "train" / src_img.name)
                shutil.copy2(SRC_LBL / (s + ".txt"), OUT_LBL / "train" / (s + ".txt"))
                break
    for s in val:
        for ext in [".jpg", ".jpeg", ".png", ".JPG", ".PNG"]:
            src_img = SRC_IMG / (s + ext)
            if src_img.exists():
                shutil.copy2(src_img, OUT_IMG / "val" / src_img.name)
                shutil.copy2(SRC_LBL / (s + ".txt"), OUT_LBL / "val" / (s + ".txt"))
                break

print("Done splitting. Train/Val folders created under data/images_split and data/labels_split")
