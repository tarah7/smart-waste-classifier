from PIL import Image,UnidentifiedImageError
from pathlib import Path

dataset_path=Path("data/raw/TrashNet")

IMAGE_EXTENSIONS={".jpg",".png",".jpeg",".bmp",".webp"}

def read_image_size(file):
    try:
        with Image.open(file) as image:
            return image.size
    except UnidentifiedImageError:
        print("Invalid Image")
        return None
    
def image_count(folder):
    count=0
    image_size=[]
    for file in folder.iterdir():
        if file.suffix.lower() in IMAGE_EXTENSIONS:
            size=read_image_size(file)
            if size is None:
                continue
            count+=1
            image_size.append(size)
    largest_size = max(image_size) if image_size else None
    return count,largest_size
if dataset_path.exists():
    total=0
    img_size=[]
    if dataset_path.is_dir():
        for folder in dataset_path.iterdir():
            waste=folder.name
            if folder.is_dir():
                number,largest_size=image_count(folder)
                print(waste,":",number)
                total+=number
                if largest_size is not None:
                    img_size.append(largest_size)
        print("total images:",total)
        if img_size:
            print("Largest image:",max(img_size))
    else:
        print("it is not a folder")
else:
    print("path didn't exist")