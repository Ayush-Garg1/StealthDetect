import streamlit as st
import numpy as np
import pickle

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

# Title of the web app
st.title("Credit Card Fraud Detection")

# Instructions
st.write("Enter all the features for the transaction in a comma-separated format.")
st.write("Order: Transaction Time, V1, V2, ..., V28, Transaction Amount")

# Input field for all features
features_input = st.text_input("Input Features (comma-separated)")

# Button for prediction
if st.button("Predict"):
    try:
        # Split the input string into a list of floats
        input_data = np.array([list(map(float, features_input.split(',')))])

        # Check if the correct number of features are provided
        if input_data.shape[1] != 30:
            st.error("Error: Please enter exactly 30 features (Transaction Time, V1-V28, Transaction Amount).")
        else:
            # Predict the result (0: Legitimate, 1: Fraudulent)
            prediction = model.predict(input_data)
            if prediction[0] == 1:
                st.error("The transaction is predicted to be FRAUDULENT.")
            else:
                st.success("The transaction is predicted to be LEGITIMATE.")
    except ValueError:
        st.error("Error: Please ensure all inputs are numeric and separated by commas.")