import json

def comment_get_started():
    with open('get-started.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Cell 1: import mlflow
    nb['cells'][1]['source'] = [
        "# Import the MLflow library to enable experiment tracking\n",
        "import mlflow"
    ]
    
    # Cell 2: mlflow.set_tracking_uri
    nb['cells'][2]['source'] = [
        "# Connect to the local MLflow tracking server running on port 5000\n",
        "mlflow.set_tracking_uri(\"http://127.0.0.1:5000\")"
    ]
    
    # Cell 3: mlflow.set_experiment
    nb['cells'][3]['source'] = [
        "# Create or set the active experiment where our runs will be logged\n",
        "mlflow.set_experiment(\"check localhost connection\")\n",
        "\n",
        "# Start a new MLflow run to log metrics\n",
        "with mlflow.start_run():\n",
        "    # Log some dummy metrics for testing out the connection\n",
        "    mlflow.log_metric(\"test\",1)\n",
        "    mlflow.log_metric(\"naveen\",2)"
    ]
    
    # Cell 4
    nb['cells'][4]['source'] = [
        "# Start another run to see how multiple runs are recorded under the same experiment\n",
        "with mlflow.start_run():\n",
        "    mlflow.log_metric(\"test-1\",1)\n",
        "    mlflow.log_metric(\"naveen-1\",2)"
    ]

    # Cell 5
    nb['cells'][5]['source'] = [
        "# Start a third run logging slightly different metrics\n",
        "with mlflow.start_run():\n",
        "    mlflow.log_metric(\"test-2\",1)\n",
        "    mlflow.log_metric(\"naveen-2\",2)"
    ]
    
    with open('get-started.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
        
def comment_gettingstarted():
    filepath = '1-MLproject/gettingstarted.ipynb'
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            src = cell['source']
            if len(src) > 0:
                if "import pandas" in src[0] and "LogisticRegression" in "".join(src):
                    cell['source'] = [
                        "# Import required libraries including pandas, scikit-learn for modeling, and mlflow for tracking\n"
                    ] + src
                elif "mlflow.set_tracking_uri" in "".join(src):
                    cell['source'] = [
                        "# Set tracking URI to point to our local MLflow server\n"
                    ] + src
                elif "LogisticRegression(" in "".join(src) and "train_test_split" in "".join(src):
                    # Already has comments like "## load the iris dataset", replace them with beginner-friendly ones
                    new_src = []
                    for line in src:
                        if line.startswith("## load the iris dataset"):
                            new_src.append("# Load the Iris flower dataset (features in x, labels in y)\n")
                        elif line.startswith("## split the data"):
                            new_src.append("# Split the dataset into 80% training data and 20% testing data to evaluate the model later\n")
                        elif line.startswith("## define the model hyperparameters"):
                            new_src.append("# Define the parameters for the Logistic Regression model (controls how the model learns)\n")
                        elif line.startswith("## train the model"):
                            new_src.append("# Initialize the model with the parameters and train it on the training data\n")
                        else:
                            new_src.append(line)
                    cell['source'] = new_src
                elif "x_test" in "".join(src) and "predict" in "".join(src):
                    new_src = []
                    for line in src:
                        if line.startswith("## predict the test set"):
                            new_src.append("# Display the test data to see what the model will make predictions on\n")
                        else:
                            new_src.append(line)
                    cell['source'] = new_src
                    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

if __name__ == "__main__":
    comment_get_started()
    comment_gettingstarted()
    print("Successfully added beginner-friendly comments to notebooks!")
