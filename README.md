# MLflow Starter Kit 🚀

Welcome to the **MLflow Starter Kit**! This repository is designed to help you quickly understand and implement [MLflow](https://mlflow.org/), an open-source platform for managing the end-to-end machine learning lifecycle.

This project includes beginner-friendly, well-commented Jupyter Notebooks that demonstrate how to:
- Connect to an MLflow Tracking Server.
- Create experiments and log multiple runs.
- Train a simple Machine Learning model (Logistic Regression on the Iris dataset).
- Track model parameters, metrics, and models using MLflow.

## 📁 Repository Structure

- `requirements.txt`: Python dependencies required for the project.
- `get-started.ipynb`: A simple notebook demonstrating how to connect to MLflow and log basic dummy metrics under an experiment.
- `1-MLproject/gettingstarted.ipynb`: A practical workflow training a Logistic Regression model on the Iris dataset, showcasing how to track hyper-parameters and models.
- `add_comments.py`: A utility script used to inject beginner-friendly explanations into the notebooks.

## 🛠️ Prerequisites

Ensure you have the following installed:
- Python 3.8+
- Jupyter Notebook or JupyterLab

## 🚀 Setup Instructions

Follow these steps to get the project running on your local machine:

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/mlflow-starter-kit.git
cd mlflow-starter-kit
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv .venv
# On Windows
.\.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Jupyter Kernel
To ensure your notebooks use the correct environment, install the virtual environment as a Jupyter kernel:
```bash
pip install ipykernel
python -m ipykernel install --user --name=mlflow_starter --display-name "Python (MLFlow Starter)"
```

---

## 🏃‍♂️ Running the Project

### 1. Start the MLflow Tracking Server
Before running the notebooks, you need to start the tracking server locally. Open a terminal, ensure your virtual environment is activated, and run:
```bash
mlflow server --host 127.0.0.1 --port 5000
```
Keep this terminal window open. You can view the MLflow UI by navigating to `http://127.0.0.1:5000` in your web browser.

### 2. Launch Jupyter Notebook
Open a new terminal, activate your environment, and start Jupyter:
```bash
jupyter notebook
```

### 3. Run the Notebooks!
Open `get-started.ipynb` or `1-MLproject/gettingstarted.ipynb`. **Important:** Make sure to select the `Python (MLFlow Starter)` kernel from the top right corner of the notebook before running the cells!

---

## 🤝 Contributing
Feel free to fork this repository and submit pull requests to add more advanced MLflow examples!

