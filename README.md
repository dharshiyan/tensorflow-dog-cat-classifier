# 🐶🐱 Dog vs Cat Image Classification using Deep Learning

This project implements a **Convolutional Neural Network (CNN)** using **TensorFlow/Keras** to classify images of **dogs and cats**.
It follows a **clean dataset structure**, **professional project layout**, and is suitable for **academic projects, internships, and GitHub portfolios**.

---

## 📂 Project Structure

```
dog-cat-classifier/
│
├── dataset/
│   ├── train/
│   │   ├── cats/
│   │   └── dogs/
│   │
│   ├── validation/
│       ├── cats/
│       └── dogs/
│
├── cat.jpg                      # Sample cat image
├── dog.jpg                      # Sample dog image
├── dog_cat_classifier.keras     # Trained Keras model
├── Figure_1.png                 # Training accuracy/loss graph
├── Figure_2.png                 # Validation accuracy/loss graph
├── train.py                     # Model training script
├── test.py                      # Model testing / inference script
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
```

---

## 🚀 Features

* Binary image classification (Dog vs Cat)
* CNN built using **TensorFlow & Keras**
* Organized dataset structure (train / validation)
* Model evaluation with accuracy graphs
* Trained model saved in **native Keras format**
* Easy to run on **local system**

---

## 🧠 Technologies Used

* Python 3.9
* TensorFlow / Keras
* NumPy
* Matplotlib
* Pillow (PIL)
* SciPy

---

## 📊 Dataset Structure

The dataset follows the standard Keras directory format:

```
dataset/
├── train/
│   ├── cats/
│   └── dogs/
│
├── validation/
    ├── cats/
    └── dogs/
```

* Images in `cats/` → Label **0**
* Images in `dogs/` → Label **1**

---

## ⚙️ Installation & Setup

### Model link

```bash
https://www.kaggle.com/models/dharshiyanacc/dog-cat-classifier
```

### Dataset link 

```bash
https://www.kaggle.com/datasets/dharshiyanacc/dog-vs-cat
```

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/dog-cat-classifier.git
cd dog-cat-classifier
```

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Training the Model

Run the training script:

```bash
python train.py
```

* Trains the CNN model
* Saves the trained model as:

  ```
  dog_cat_classifier.keras
  ```
* Generates training & validation accuracy plots

---

## 🧪 Testing / Prediction

Run the test script:

```bash
python test.py
```

Use sample images like:

* `cat.jpg`
* `dog.jpg`

---

## 📈 Results

* Training and validation accuracy graphs are saved as:

  * `Figure_1.png`
  * `Figure_2.png`
* Model achieves reliable classification performance on validation data

---

## 💾 Model Format

The trained model is saved using **native Keras format**:

```
dog_cat_classifier.keras
```

### Why `.keras` format?

* Recommended by TensorFlow
* Preserves model architecture + weights
* Better forward compatibility than `.h5`

---

## 📌 Future Improvements

* Add test dataset
* Data augmentation
* Transfer learning (MobileNet / ResNet)
* Convert model to TensorFlow Lite
* Build a web interface for predictions

---

## 👨‍💻 Author

DHARSHIYAN -
Deep Learning & Computer Vision Enthusiast

---

## 📄 License
This project is licensed under the MIT License.
