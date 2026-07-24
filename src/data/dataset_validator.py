from pathlib import Path
from PIL import Image, UnidentifiedImageError

IMAGE_EXTENSIONS = {".jpg", ".png", ".jpeg", ".bmp", ".webp"}

SMALL_WIDTH = 100
SMALL_HEIGHT = 100


def is_valid_image(file):
    
    try:
        with Image.open(file) as image:
            image.verify()

        return 1, 0

    except (UnidentifiedImageError, OSError):
        return 0, 1


def check_image_size(file):
    

    with Image.open(file) as image:
        width, height = image.size

    if width < SMALL_WIDTH or height < SMALL_HEIGHT:
        return 1

    return 0


def validate_dataset():

    dataset_path = Path("data/raw/TrashNet")

    total = 0
    valid = 0
    corrupted = 0
    unsupported = 0
    small = 0

    if not dataset_path.exists():
        print("Path doesn't exist.")
        return

    if not dataset_path.is_dir():
        print("Not a directory.")
        return

    for folder in dataset_path.iterdir():

        if not folder.is_dir():
            continue

        for file in folder.iterdir():

            # Skip unsupported files
            if file.suffix.lower() not in IMAGE_EXTENSIONS:
                unsupported += 1
                continue

            total += 1

            valid_images, corrupted_images = is_valid_image(file)

            valid += valid_images
            corrupted += corrupted_images

            # Only check size if the image is valid
            if valid_images:
                small += check_image_size(file)

    return total, valid, corrupted, unsupported, small


def print_validation_report():

    (
        total,
        valid,
        corrupted,
        unsupported,
        small,
    ) = validate_dataset()

    print("\nDataset Validation Report")
    print("-------------------------")
    print(f"Total Images      : {total}")
    print(f"Valid Images      : {valid}")
    print(f"Corrupted Images  : {corrupted}")
    print(f"Unsupported Format: {unsupported}")
    print(f"Small Images      : {small}")
    print("-------------------------")
    print("Validation Complete.")


print_validation_report()