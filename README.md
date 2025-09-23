# Amazon Review Sentiment Analysis

This project applies **Natural Language Processing (NLP)** and **Machine Learning** to classify Amazon product reviews as **positive** or **negative**.  
It demonstrates end-to-end data science skills: from text preprocessing and model training to deploying a working web application with Flask.

---

## 🚀 Features
- Preprocessing: tokenization, stopword removal, TF-IDF vectorisation
- Models: Logistic Regression, Multinomial Naïve Bayes, Random Forest
- Achieved **~85–90% accuracy** on test data
- Interactive **Flask web app** for real-time review sentiment prediction
- Visualisations: sentiment distribution, word frequencies, confusion matrices

---

## 📊 Dataset
- Source: [Amazon Fine Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)  
- 568k+ reviews with ratings (1–5 stars) mapped into binary classes:  
  - 1–2 ⭐ → Negative  
  - 4–5 ⭐ → Positive  
  - 3 ⭐ → Neutral (excluded)

---

## 🛠️ Tech Stack
- Python  
- Pandas, NumPy, Scikit-learn, Matplotlib  
- Flask (for deployment)
- 
---

---

## ⚡ How to Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/Adamh25/Amazon-sentiment-analysis.git
   cd Amazon-sentiment-analysis
2. Create a conda environment and install dependencies:

conda create -n nlp_project python=3.10
conda activate nlp_project
conda install -c conda-forge pandas scikit-learn matplotlib flask nltk

3. Run the Jupyter notebook to train models and save artifacts.

4. Start the Flask app:

cd sentiment_app
python app.py

Open http://127.0.0.1:5000
 in your browser and test reviews.

🔮 Future Improvements

Add neutral class support (3-star reviews)

Deploy app online (Heroku/Render/PythonAnywhere)

Experiment with deep learning models (LSTMs, BERT)


## 📂 Project Structure
