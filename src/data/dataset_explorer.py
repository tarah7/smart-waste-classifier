from pathlib import Path
from PIL import Image, UnidentifiedImageError

dataset_path = Path("data/raw/TrashNet")

IMAGE_EXTENSIONS = {".jpg", ".png", ".jpeg", ".bmp", ".webp"}
IMAGE_MODE = {"RGB", "L", "RGBA"}


def read_image(image):

    rgb = 0
    l = 0
    rgba = 0

    if image.mode == "RGB":
        rgb = 1
    elif image.mode == "L":
        l = 1
    elif image.mode == "RGBA":
        rgba = 1

    size = image.size

    return size, rgb, l, rgba


def count_class(folder):
    
    count = 0

    total_rgb = 0
    total_l = 0
    total_rgba = 0

    image_sizes = []

    corrupted = 0

    for file in folder.iterdir():

        if file.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        try:
            with Image.open(file) as image:

                size, rgb, l, rgba = read_image(image)

                total_rgb += rgb
                total_l += l
                total_rgba += rgba

                image_sizes.append(size)

                count += 1

        except UnidentifiedImageError:
            corrupted += 1

    return (
        count,
        image_sizes,
        total_rgb,
        total_l,
        total_rgba,
        corrupted,
    )


def analyze_dataset(dataset_path):

    if not dataset_path.exists():
        print("Path doesn't exist.")
        return

    if not dataset_path.is_dir():
        print("Not a directory.")
        return

    total_images = 0

    total_rgb = 0
    total_l = 0
    total_rgba = 0

    corrupted_images = 0

    all_image_sizes = []

    for folder in dataset_path.iterdir():

        if not folder.is_dir():
            continue

        (
            count,
            image_sizes,
            rgb,
            l,
            rgba,
            corrupted,
        ) = count_class(folder)

        print(f"{folder.name}: {count}")

        total_images += count

        total_rgb += rgb
        total_l += l
        total_rgba += rgba

        corrupted_images += corrupted

        all_image_sizes.extend(image_sizes)

    print("\nDataset Report")
    print("-" * 30)

    print("Total Images :", total_images)

    print("RGB :", total_rgb)
    print("L :", total_l)
    print("RGBA :", total_rgba)

    print("Corrupted :", corrupted_images)

    if all_image_sizes:
        print("Smallest :", min(all_image_sizes))
        print("Largest :", max(all_image_sizes))


analyze_dataset(dataset_path)