
#  Gender Prediction System

##  Overview
Leverage a **Random Forest Classifier** to predict gender based on physical attributes such as **height**, **weight**, and **voice pitch**. This project includes end-to-end preprocessing, model training, evaluation, and an interactive Flask web interface for real-time predictions.

---

##  Table of Contents
- [⚙️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [📁 Project Structure](#-project-structure)  
- [📊 Results](#-results)  
- [🤝 Contributing](#-contributing)  
- [📬 Contact](#-contact)  

---

##  Installation

```bash
git clone https://github.com/Srinithimahalakshmi/Geneder_prediction.git
cd Geneder_prediction

python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
````

---

## Usage

### 1. Run the Jupyter Notebook (Optional)

Explore preprocessing, training, and evaluation in detail:

```bash
jupyter notebook model_training.ipynb
```

### 2. Train & Evaluate the Model

```bash
python src/data_preprocessing.py
python src/train_model.py
python src/evaluate_model.py --model models/random_forest.pkl
```

### 3. Launch the Flask Web App

```bash
python app.py
```

Then visit **[http://127.0.0.1:5000](http://127.0.0.1:5000)** to input sample data and get instant predictions!

---

## Project Structure

```
Geneder_prediction/
│
├── data/                     
│   └── gender_data.csv              # Dataset for model training
│
├── notebooks/                
│   └── model_training.ipynb        # EDA and model development notebook
│
├── src/
│   ├── data_preprocessing.py       # Data cleaning & feature preparation
│   ├── train_model.py              # Model training pipeline
│   ├── evaluate_model.py           # Evaluation metrics and reporting
│   └── predict.py                  # Prediction module or CLI support
│
├── models/
│   └── random_forest.pkl           # Serialized trained model
│
├── app.py                          # Flask web application
├── templates/
│   └── index.html                  # Web interface template
│
├── static/
│   └── style.css                   # Styling for the web app
│
├── requirements.txt                # Project dependencies
└── README.md                       # This documentation
```

---

## Results

* **Accuracy**: `XX%`
* **Precision / Recall / F1-Score**: `YY% / ZZ% / AA%`

Include visuals like confusion matrices or performance charts here or in the notebook for added clarity.

---

## Contributing

I'd love your help! You could:

* Add alternate models (e.g., XGBoost, SVM)
* Improve feature engineering or preprocessing
* Enhance visualizations and model interpretability with SHAP
* Upgrade the UI–perhaps add CLI options or input validation

**To contribute:**

1. Fork the repo
2. Create your branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m "Add feature XYZ"`)
4. Push and open a Pull Request

---

## Contact

👤 **Maintainer**: Srinithi Mahalakshmi
📧 **Email**: [srinithiarumugam2003@gmail.com](mailto:srinithiarumugam2003@gmail.com)
🔗 **GitHub**: [Srinithimahalakshmi](https://github.com/Srinithimahalakshmi)

---

⭐ *If this project was helpful, please consider giving it a star!*

```
