from pathlib import Path
from torchvision import transforms
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
PROCESSED_DATASET_PATH = Path("data/processed")

def get_train_transforms():
    transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    ])
    return transform

def create_datasets():

    train_folder = (
            PROCESSED_DATASET_PATH /
            "train"
        )

    validation_folder = (
            PROCESSED_DATASET_PATH /
            "validation" 
        )

    test_folder = (
            PROCESSED_DATASET_PATH /
            "test"
        )
    transform = get_train_transforms()

    training_dataset = ImageFolder(
    train_folder,
    transform=transform
    )

    validation_dataset = ImageFolder(
    validation_folder,
    transform=transform
    )

    testing_dataset = ImageFolder(
    test_folder,
    transform=transform
    )
    
    return training_dataset,validation_dataset,testing_dataset
def create_dataloaders(training_dataset,validation_dataset,testing_dataset):
    train_loader= DataLoader(
    training_dataset,
    batch_size=32,
    shuffle=True
    )
    validate_loader = DataLoader(
    validation_dataset,
    batch_size=32,
    shuffle=True
    )
    test_loader = DataLoader(
    testing_dataset,
    batch_size=32,
    shuffle=True
    )
    return train_loader,validate_loader,test_loader