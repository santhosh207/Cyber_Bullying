import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def make_prediction(text):
    data = pd.read_csv('public.csv')
    texts = data['full_text']
    labels = data['label']
    texts_train, texts_val, labels_train, labels_val = train_test_split(texts, labels, test_size=0.2, random_state=42)
    vectorizer = CountVectorizer()
    features_train = vectorizer.fit_transform(texts_train)
    features_val = vectorizer.transform(texts_val)
    model = LogisticRegression()
    model.fit(features_train, labels_train)
    def load_model_and_predict(text):
        text_vector = vectorizer.transform([text])
        prediction = model.predict(text_vector)
        return prediction[0]
    new_text = text
    prediction = load_model_and_predict(new_text)
    return prediction

