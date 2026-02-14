import pickle

with open("models/intent_classifier.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

def predict_intent(query):
    query_vec = vectorizer.transform([query])
    return model.predict(query_vec)[0]
