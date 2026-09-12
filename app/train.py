from src.data.dataloader import create_datasets, create_dataloaders
from src.models.waste_classifier import WasteClassifier
from src.training.trainer import train_one_epoch, validate_one_epoch,evaluate_accuracy
import torch.nn as nn
import torch
train_dataset, validation_dataset, test_dataset = create_datasets()
train_loader, validation_loader, test_loader = create_dataloaders(
    train_dataset,
    validation_dataset,
    test_dataset,
)
model = WasteClassifier()
loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)
for epoch in range(5):
    train_loss = train_one_epoch(model, train_loader, loss_function, optimizer)
    validation_loss = validate_one_epoch(model, validation_loader, loss_function)
    print(f"Epoch {epoch + 1}")
    print(f"Training Loss: {train_loss:.4f}")
    print(f"Validation Loss: {validation_loss:.4f}")
test_accuracy = evaluate_accuracy(model, test_loader)
print(f"Test Accuracy: {test_accuracy:.4f}")