## Car Sales Prediction

This project aims to predict the sale price of vehicles based on various features such as year, make, transmission, state, condition, odometer reading, color, and interior. The machine learning model is trained on historical car sales data.
https://github.com/BiswajitJena2002/Car_Sales_Prediction/assets/121337717/c3dbd762-eea5-49bd-a619-27464ca877ac

### Model.ipynb

This Jupyter Notebook contains the data preprocessing, exploratory data analysis, model training, evaluation, and saving the trained model. Here's a brief overview of the contents:

- **Data Preprocessing**: Handling missing values, encoding categorical variables, and preparing the data for analysis.
- **Descriptive Analysis**: Providing statistical summaries and distributions of the dataset.
- **Data Visualization**: Utilizing visualizations to explore relationships between features and the target variable.
- **Model Training**: Implementing various regression models such as Linear Regression, Ridge Regression, Lasso Regression, Random Forest Regression, KNeighborsRegressor, and DecisionTreeRegressor.
- **Model Evaluation**: Assessing model performance using Mean Squared Error (MSE) and R-squared (R2) scores.
- **Saving the Model**: Exporting the best-performing model and the fitted scaler for deployment.

### app.py

This Flask application serves as the deployment endpoint for the trained model. It includes routes for rendering the web interface and making predictions based on user input. Here are the key functionalities:

- **Index Route**: Renders the HTML form for users to input vehicle details.
- **Predict Route**: Processes the form input, scales the features, and predicts the sale price using the pre-trained model.
- **Model Loading**: Loads the pre-trained model and the fitted scaler for prediction.

### Other Files

- **Car_Sales_rf.joblib**: Serialized file containing the trained Random Forest Regression model.
- **Car_Sales_scaler.joblib**: Serialized file containing the fitted scaler for feature scaling.
- **car_prices.csv**: Dataset used for training the machine learning model.
- **requirements.txt**: File specifying the dependencies required to run the Flask application.

### Usage

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application using `python app.py`.
4. Open your web browser and go to `http://localhost:5000` to access the prediction interface.

Feel free to explore the notebook for detailed analysis and model training steps. I
