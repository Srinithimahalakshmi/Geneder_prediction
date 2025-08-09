
# Gender Prediction Using Decision Tree Algorithm

This project aims to classify gender (Male/Female) based on various features such as height, weight, and voice pitch using the Decision Tree algorithm. The dataset comprises attributes that are commonly associated with gender differences, and the model is trained to predict gender with high accuracy.

## 📂 Project Structure

```
Gender_Prediction/
│
├── data/
│   └── voice.csv             # Dataset containing features and gender labels
│
├── notebooks/
│   └── model_training.ipynb  # Jupyter notebook for data preprocessing, model training, and evaluation
│
└── app.py                    # Flask application for deploying the model as a web service
```

## 📊 Dataset Overview

The `voice.csv` dataset includes the following features:

- **height**: Height of the individual (in cm)
- **weight**: Weight of the individual (in kg)
- **pitch**: Voice pitch (in Hz)
- **label**: Gender label (Male/Female)

## ⚙️ Decision Tree Algorithm

The Decision Tree algorithm is a supervised machine learning method used for classification and regression tasks. It splits the data into subsets based on feature values, creating a tree-like structure where each node represents a decision based on a feature, and each leaf node represents an outcome.

### Key Concepts:

- **Root Node**: The top node representing the entire dataset.
- **Decision Nodes**: Nodes that split the data based on feature values.
- **Leaf Nodes**: Terminal nodes that represent the final classification.
- **Splitting**: The process of dividing a node into sub-nodes.
- **Pruning**: Removing sections of the tree that do not provide additional value.

### Advantages:

- Easy to understand and interpret.
- Handles both numerical and categorical data.
- Requires little data preprocessing.

### Disadvantages:

- Prone to overfitting, especially with complex trees.
- Sensitive to noisy data.

## 🚀 Model Training

The model is trained using the following steps:

1. **Data Preprocessing**: Handling missing values, encoding categorical variables, and scaling features.
2. **Feature Selection**: Identifying the most relevant features for the model.
3. **Model Training**: Using the Decision Tree algorithm to train the model on the dataset.
4. **Model Evaluation**: Assessing the model's performance using metrics like accuracy, precision, recall, and F1-score.

## 🌐 Web Application

The `app.py` file contains a Flask application that serves the trained model as a web service. Users can input their features through a web interface, and the model will predict the gender.

## 📈 Results

The Decision Tree model achieved an accuracy of approximately 85% on the test set, demonstrating its effectiveness in gender classification tasks.

## 📥 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Srinithimahalakshmi/Geneder_prediction.git
   cd Geneder_prediction
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000` to use the gender prediction web service.

## 📚 References

- [IBM: What is a Decision Tree?](https://www.ibm.com/think/topics/decision-trees)
- [KDnuggets: Decision Tree Algorithm, Explained](https://www.kdnuggets.com/2020/01/decision-tree-algorithm-explained.html)
- [GeeksforGeeks: Decision Tree](https://www.geeksforgeeks.org/machine-learning/decision-tree/)
