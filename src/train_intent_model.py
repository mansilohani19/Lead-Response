import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load data
df = pd.read_csv("data/sample_training_data.csv")

X = df["text"]
y = df["intent"]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

# Save model
with open("models/intent_classifier.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("Intent classifier trained and saved.")
