import torch
from sklearn.metrics import confusion_matrix, classification_report
from src.data.dataloader import create_datasets, create_dataloaders
from src.models.waste_classifier import WasteClassifier

model = WasteClassifier()

model.load_state_dict(
    torch.load("models/waste_classifier.pth")
)

actual_labels = []
predicted_labels = []
train_dataset, validation_dataset, test_dataset = create_datasets()

train_loader, validation_loader, test_loader = create_dataloaders(
    train_dataset,
    validation_dataset,
    test_dataset,
)

model.eval()

with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        actual_labels.extend(labels.tolist())
        predicted_labels.extend(predicted.tolist())
print(confusion_matrix(
    actual_labels,
    predicted_labels
))

class_names = test_dataset.classes

print(classification_report(
    actual_labels,
    predicted_labels,
    target_names=class_names
))