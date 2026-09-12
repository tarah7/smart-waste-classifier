from pathlib import Path

from PIL import Image

from src.inference.predictor import load_model, predict_image


TEST_FOLDER = Path("data/processed/test/plastic")

image_files = list(TEST_FOLDER.glob("*.jpg"))

if not image_files:
    print("No test images found.")
else:
    image_path = image_files[0]

    image = Image.open(image_path)

    model = load_model()

    predicted_class, confidence = predict_image(
        model,
        image
    )

    print(f"Image: {image_path.name}")
    print(f"Prediction: {predicted_class}")
    print(f"Confidence: {confidence:.2%}")