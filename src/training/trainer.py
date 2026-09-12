import torch
import torch.nn as nn

def train_one_epoch(model, train_loader, loss_function, optimizer):
    model.train()
    total_loss = 0.0
    for images, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = loss_function(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss +=loss.item()
    average_loss = total_loss / len(train_loader)
    return average_loss
def validate_one_epoch(model, validation_loader, loss_function):
    model.eval()
    total_loss = 0.0
    with torch.no_grad():
        for images, labels in validation_loader:
            outputs = model(images)
            loss = loss_function(outputs, labels)
            total_loss += loss.item()
    average_loss = total_loss / len(validation_loader)
    return average_loss
def evaluate_accuracy(model, data_loader):
    model.eval()
    total = 0
    correct=0
    with torch.no_grad():
        for images, labels in data_loader:
            outputs = model(images)
            _,predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)
    accuracy = correct / total
    return accuracy