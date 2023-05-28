import streamlit as st
import requests
import json
import main
# Define the Flask server URL
FLASK_SERVER_URL = 'http://localhost:8501'


# Create the Streamlit app
def main():
    st.title("Offensiveness Classifier")
    text = st.text_input("Enter text")
    if st.button("Predict"):
        prediction = make_prediction(text)
        if prediction is not None:
            if prediction == 1:
                print("the text is offesive")
                st.write("The text is offensive.")
            else:
                print("text is non-offensive")
                st.write("The text is non-offensive.")


# Create a function to make a request to the Flask server
def make_prediction(text):
    data = {'text': text}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f'{FLASK_SERVER_URL}/predict', data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        try:
            prediction = response.json()['prediction']
            return prediction
        except ValueError as e:
            print(f"JSON decoding error: {e}")
    else:
        print(f"Request failed with status code: {response.status_code}")

    return None


if __name__ == '__main__':
    main()
