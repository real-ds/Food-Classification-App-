import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import requests

# Nutritionix API credentials
NUTRITIONIX_APP_ID = "acb1989c"  # Replace with your App ID
NUTRITIONIX_API_KEY = "86c15a137fdf590255e5038237cf001b"  # Replace with your API Key
API_URL = "https://trackapi.nutritionix.com/v2/natural/nutrients"

# Load the MobileNetV2 model
@st.cache_resource
def load_model():
    model = MobileNetV2(weights="imagenet")
    return model

# Image preprocessing
def preprocess_image(image):
    image = image.resize((224, 224))  # MobileNetV2 input size
    image_array = np.array(image)
    image_array = preprocess_input(image_array)
    return np.expand_dims(image_array, axis=0)

# Fetch calorie information from Nutritionix
def fetch_calorie_info(food_item, portion_size):
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
        "Content-Type": "application/json",
    }
    payload = {"query": f"{portion_size} {food_item}"}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        if "foods" in data and len(data["foods"]) > 0:
            calories = data["foods"][0]["nf_calories"]
            return round(calories, 2)
    return "Unknown"

# Main Streamlit app
st.title("Enhanced Food Classification and Calorie Estimation")
st.write("Upload a food image, and the system will classify it, estimate its calorie value based on portion size, and provide a confidence score.")

# File uploader
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Load model and classify image
    model = load_model()
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    # Display top prediction
    top_prediction = decoded_predictions[0]
    class_name, confidence = top_prediction[1], top_prediction[2]

    # Ask for portion size
    portion_size = st.number_input(
        "Enter Portion Size (e.g., 1 slice, 1 cup, etc.)", min_value=1, step=1, format="%d"
    )
    if portion_size > 0:
        calorie_value = fetch_calorie_info(class_name.lower(), portion_size)

        st.write(f"### Prediction: {class_name.capitalize()}")
        st.write(f"**Confidence:** {confidence:.2f}")
        st.write(f"**Estimated Calories:** {calorie_value} kcal (based on {portion_size} portion)")

    # Display top-3 predictions for more context
    st.write("### Top-3 Predictions")
    for i, pred in enumerate(decoded_predictions, start=1):
        st.write(f"{i}. {pred[1].capitalize()} ({pred[2]:.2f} confidence)")
