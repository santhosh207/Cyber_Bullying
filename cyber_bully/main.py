from flask import Flask, request, jsonify
import pickle
import app1
from flask_cors import CORS
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
CORS(app)

model = LogisticRegression()
vectorizer = CountVectorizer()

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Dump the vectorizer object to a pickle file
with open('vectorizer.pkl', 'wb') as file:
    pickle.dump(vectorizer, file)

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
    processed_text = preprocess_text(text)
    text_vector = vectorizer.transform([processed_text])
    prediction = model.predict(text_vector)
    return jsonify({'prediction': int(prediction[0])})

# Preprocess the text
def preprocess_text(text):
    # Apply any necessary preprocessing steps to the text
    # e.g., lowercase, remove punctuation, etc.
    return text.lower()

if __name__ == '__main__':
    app.run(debug=True)
