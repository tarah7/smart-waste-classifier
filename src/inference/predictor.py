from pathlib import Path

import torch
from PIL import Image
from torchvision import transforms

from src.models.waste_classifier import WasteClassifier


MODEL_PATH = Path("models/waste_classifier.pth")

CLASS_NAMES = [
    "cardboard",
    "glass",
    "metal",
    "paper",
    "plastic",
    "trash",
]


def load_model():
    model = WasteClassifier()

    model.load_state_dict(
        torch.load(
            MODEL_PATH,
            map_location=torch.device("cpu")
        )
    )

    model.eval()

    return model


def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    image = transform(image)
    image = image.unsqueeze(0)

    return image


def predict_image(model, image):
    image = preprocess_image(image)

    with torch.no_grad():
        outputs = model(image)

        probabilities = torch.softmax(
            outputs,
            dim=1
        )

        confidence, predicted_index = torch.max(
            probabilities,
            dim=1
        )

    predicted_class = CLASS_NAMES[predicted_index.item()]
    confidence = confidence.item()

    return predicted_class, confidence