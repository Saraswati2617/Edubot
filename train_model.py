import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\new project\data\dataset.csv")

# Text classification pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("model", MultinomialNB())
])

# Train the model
X = df["input_text"]
y = df["field"]
pipeline.fit(X, y)

# Save the model
joblib.dump(pipeline, "model/model.pkl")
print("Model saved!")
