
# Food Classification App

Food Classification App is a machine learning-based Python application that allows users to classify food items based on images. This app leverages a pre-trained model to predict the food category of any image uploaded by the user.

## Try it out

https://foodclassificationapp.streamlit.app/


## Installation
To install and run the Food Classification App locally, follow the steps below:

Clone this repository:

bash
```
git clone https://github.com/your-username/food-classification-app.git
Navigate to the project directory:
```
bash
```
cd food-classification-app
```
For Windows:

```
python -m venv env
.\env\Scripts\activate
```
For macOS/Linux:
```
python3 -m venv env
source env/bin/activate
```
Install the required dependencies:
```
pip install -r requirements.txt
Usage
```

Once the app is set up and dependencies are installed, run the Streamlit app:

```
streamlit run app.py
```
Open a web browser and go to 
 to start using the app.

 http://localhost:8501 
 

Upload food images and get predictions on the food category.

## Upload an image file
```
image = st.file_uploader("Upload a Food Image", type=["jpg", "png", "jpeg"])

if image:
    # Call prediction function
    prediction = predict_food(image)
    st.write(f"Predicted Food Category: {prediction}")

```
Contributing
Pull requests are welcome. If you're planning to make major changes, please open an issue to discuss what you'd like to change.

To contribute:

Fork this repository.
Create a new branch (
```
git checkout -b feature-name
```
Make your changes and commit them (
```
git commit -am 'Add new feature'
```
Push to the branch 
```
git push origin feature-name
```
Create a pull request.
Please make sure to update tests as appropriate.

License
This project is licensed under the MIT License.



