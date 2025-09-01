import os

image_dir = 'images'
label_dir = 'labels'

images = [f.lower().replace('.jpg', '.txt') for f in os.listdir(image_dir) if f.lower().endswith('.jpg')]
labels = [f for f in os.listdir(label_dir) if f.endswith('.txt')]

deleted = 0
for lbl in labels:
    if lbl.lower() not in images:
        os.remove(os.path.join(label_dir, lbl))
        deleted += 1

print(f"Deleted {deleted} extra labels. Images: {len(os.listdir(image_dir))}, Labels: {len(os.listdir(label_dir))}")