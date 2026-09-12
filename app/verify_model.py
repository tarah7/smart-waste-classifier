from src.data.dataloader import create_datasets, create_dataloaders
from src.models.waste_classifier import WasteClassifier
train_dataset, validation_dataset, test_dataset = create_datasets()
train_loader, validation_loader, test_loader = create_dataloaders(
    train_dataset,
    validation_dataset,
    test_dataset,
)
images, labels = next(iter(train_loader))
model = WasteClassifier()
model.eval()
outputs = model(images)
print(images.shape)
print(labels.shape)
print(outputs.shape)