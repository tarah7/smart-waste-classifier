from PIL import Image,UnidentifiedImageError
from pathlib import Path

dataset_path=Path("data/raw/TrashNet")

IMAGE_EXTENSIONS={".jpg",".png",".jpeg",".bmp",".webp"}

IMAGE_MODE={"RGB","L","RGBA"}

def read_image(image):
    rgb=0
    l=0
    rgba=0
    if image.mode=="RGB":
        rgb=1
    elif image.mode=="L":
        l=1
    elif image.mode=="RGBA":
        rgba=1
    size=image.size
    return size,rgb,l,rgba

def count_class(folder):
    count=0
    r=0
    la=0
    rg=0
    image_size=[]
    corrupted = 0
    for file in folder.iterdir():

        if file.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        try:
            with Image.open(file) as image:
                size,rgb,l,rgba=read_image(image)
                r+=rgb
                la+=l
                rg+=rgba

                count+=1
            if size is not None:
                image_size.extende(image_size)
        except UnidentifiedImageError:
            corrupted += 1

    return count,r,la,rg,image_size,corrupted

if dataset_path.exists():
        total=0
        img_size=[]
        r=0
        la=0
        rg=0
        corrupted_images = 0
        if dataset_path.is_dir():

            for folder in dataset_path.iterdir():

                item=folder.name
                if folder.is_dir():

                    count,rgb,l,rgba,image_size,corrupted=count_class(folder)
                    print(item,":",count)
                    total+=count
                    r+=rgb
                    all_image_size = []
                    la+=l
                    rg+=rgba
                    corrupted_images+= corrupted
                    all_image_size.extend(image_size)
            print("total images:",total)
            if r:
                 print("RGB:",r)
            if la:
                print("L:",la)
            if rg:
                print('RGBA:',rg)
            print("Corrupted :", corrupted_images)
            if all_image_size:
                print("Smallest :", min(all_image_size))
                print("Largest :", max(all_image_size))

        else:

            print("it is not a folder")

else:
    
    print("path didn't exist")