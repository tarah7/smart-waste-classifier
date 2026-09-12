# Smart Waste Classifier

A small computer vision project built to explore my interest in Machine Learning, Deep Learning, and Computer Vision.

The goal of this project is to build a simple waste image classifier that can identify different types of waste from an uploaded image or a camera image.

🎯 Why I Built This

I built this project mainly to learn and understand my interest in Machine Learning and Computer Vision by actually building something.

This is not intended to be a production-ready waste-management system. The project is a practical learning experiment that helped me understand the workflow of a machine learning application, from dataset preparation and model training to evaluation and deployment.

🗂️ Classes

The model was trained to classify images into these six classes:

Cardboard

Glass

Metal

Paper

Plastic

Trash

Note: The current model does not classify Organic or E-waste. Those categories were part of the original idea, but the dataset used for this version contains the six classes listed above.

🧠 Model

The project uses a custom Convolutional Neural Network (CNN) built with PyTorch.

The model contains:

Convolutional layers

ReLU activation

Max pooling

Adaptive average pooling

Fully connected classification layer

Input images are resized to 224 × 224 pixels.

📊 Model Accuracy

The final test accuracy was approximately:

44.58%

The accuracy is relatively low, and I am intentionally mentioning it because this project is primarily a learning project, not a claim of production-level performance.

The evaluation also showed that some classes were much harder for the model to distinguish than others. For example, the model performed better on cardboard and plastic than on metal and trash.

This evaluation helped me understand an important part of machine learning: building a model is not enough. You also need to evaluate where and why it fails.

🛠️ Technologies Used

Python

PyTorch

Torchvision

OpenCV

Pillow

NumPy

Pandas

Scikit-learn

Streamlit

Git

VS Code

📁 Project Structure

Smart-Waste-Classifier/
│
├── app/
│   ├── analyze_dataset.py
│   ├── evaluate_model.py
│   ├── streamlit_app.py
│   ├── test_predictor.py
│   ├── train.py
│   ├── verify_dataloader.py
│   └── verify_model.py
│
├── assets/
│
├── data/
│   ├── external/
│   ├── processed/
│   │   ├── test/
│   │   ├── train/
│   │   └── validation/
│   └── raw/
│
├── models/
│   └── waste_classifier.pth
│
├── src/
│   ├── data/
│   │   ├── dataloader.py
│   │   ├── dataset_explorer.py
│   │   ├── dataset_splitter.py
│   │   └── dataset_validator.py
│   │
│   ├── models/
│   │   └── waste_classifier.py
│   │
│   ├── training/
│   │   └── trainer.py
│   │
│   └── inference/
│       └── predictor.py
│
└── .gitignore

🚀 Running the Application

Create and activate a virtual environment, then install the required dependencies.

Run the Streamlit application with:

python -m streamlit run app/streamlit_app.py

The application can then be opened locally in a web browser.

It supports:

📷 Camera input

🖼️ Image upload

🤖 Waste classification

📈 Prediction confidence

🔬 Machine Learning Workflow

The project follows a basic end-to-end machine learning workflow:

Dataset
   ↓
Dataset Validation
   ↓
Dataset Splitting
   ↓
DataLoader
   ↓
CNN Model
   ↓
Training
   ↓
Evaluation
   ↓
Inference
   ↓
Streamlit Application

📌 Limitations

This project has several limitations:

Test accuracy is only about 44.58%.

The model is trained on a relatively limited dataset.

Some classes are difficult to distinguish visually.

The model may produce low-confidence predictions.

The model is not suitable for real-world waste-management decisions.

The current dataset does not contain dedicated Organic and E-waste classes.

🔮 Future Improvements

If I continue developing this project, I would like to:

Improve the dataset and class balance.

Experiment with stronger CNN architectures.

Try transfer learning with pretrained models.

Add Organic and E-waste categories.

Improve image preprocessing and augmentation.

Improve confidence handling.

Add better recycling and disposal information.

Evaluate the model more extensively.

📚 What I Learned

Through this project, I practiced:

Preparing and validating an image dataset

Splitting data into training, validation, and test sets

Using PyTorch Dataset and DataLoader

Building a CNN

Training a neural network

Evaluating classification performance

Using confusion matrices and classification reports

Building an inference pipeline

Connecting a trained model to a Streamlit application

Using Git for version control

👤 Project Purpose

This project was built as a personal learning project to explore my interest in Machine Learning and Computer Vision.

The most important result for me was not achieving a high accuracy score, but understanding the complete process of taking an ML idea and turning it into a working application.

Built as a learning project with Python, PyTorch, and Streamlit. ♻️
