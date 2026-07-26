from src.data.dataloader import (
    create_datasets,
    create_dataloaders,
)
train_dataset, validation_dataset, test_dataset = create_datasets()
train_loader,validate_loader,test_loader=create_dataloaders(train_dataset,
    validation_dataset,
    test_dataset,)
print(len(train_dataset))
images, labels = next(iter(train_loader))
print(labels.shape)
print(images.shape)
print(train_dataset.classes)