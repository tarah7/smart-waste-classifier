import random
import shutil
from pathlib import Path
PROCESSED_DATASET_PATH=Path("data/processed")
FOLDERS=["train","validation","test"]
IMAGE_EXTENSIONS = {".jpg", ".png", ".jpeg", ".bmp", ".webp"}
DATASET_PATH = Path("data/raw/TrashNet")
CLASSES = [
    "cardboard",
    "glass",
    "metal",
    "paper",
    "plastic",
    "trash",
]

def get_image_files(class_folder):
    images=[]
    for file in class_folder.iterdir():   
        if file.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        images.append(file)
    return images
def shuffle_images(images):
    random.shuffle(images)
    
    return images
def calculate_split_sizes(total_images):
    train_size=int(total_images * 0.7)
    validation_size=int(total_images * 0.15)
    test_size=total_images-train_size-validation_size
    return train_size, validation_size, test_size

def split_images(images, train_size, validation_size):
    train_images = images[:train_size]

    validation_images = images[
    train_size : train_size + validation_size
    ]

    test_images = images[
    train_size + validation_size :
    ]
    return train_images,validation_images,test_images

def copy_images(image_list,destination_folder):
    for image in image_list:
        shutil.copy2(image, destination_folder / image.name)

def create_output_folders():
    for folder in FOLDERS:
        folder_name=PROCESSED_DATASET_PATH/folder
        folder_name.mkdir(parents=True, exist_ok=True)
        for trash_class in CLASSES:
            (folder_name/trash_class).mkdir(parents=True, exist_ok=True)

def prepare_dataset():
    
    if not DATASET_PATH.exists():
        print("Path doesn't exist.")
        return
    if not DATASET_PATH.is_dir():
        print("Not a directory.")
        return

    create_output_folders()

    for folder in DATASET_PATH.iterdir():
    
        if not folder.is_dir():
            continue
        images=get_image_files(folder)
        images=shuffle_images(images)
        train_size, validation_size, test_size = calculate_split_sizes(
            len(images))
        train_images, validation_images, test_images = split_images(
            images,
            train_size,
            validation_size,
        )
        train_folder = (
            PROCESSED_DATASET_PATH /
            "train" /
            folder.name
        )

        validation_folder = (
            PROCESSED_DATASET_PATH /
            "validation" /
            folder.name
        )

        test_folder = (
            PROCESSED_DATASET_PATH /
            "test" /
            folder.name
        )
        copy_images(train_images, train_folder)
        copy_images(validation_images, validation_folder)
        copy_images(test_images, test_folder)
prepare_dataset()