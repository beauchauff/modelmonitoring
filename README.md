Assignment 5: Model Monitoring

Project Description
Assignment 5 builds on the previous sentiment prediction app which has a container that is used to build and run the 
Prediction app, an app which predicts input user review text as positive or negative. A dedicated API backend has been 
created and customized to wrap this backend with Docker to prepare for deployment and pushed to a GitHub repository. 
Monitoring the model has been created to provide users with data on the outputs of the model and measure against a 
standard through a streamlit dashboard.

Prerequisites
Docker and streamlit must be installed to run app.

How to Run
Makefile is used to build and run the application with mapped commands for ease of use.
Curl commands or postman can be used for individual queries.
From the CLI, a curl command would be formatted like:
curl--user "APITest\APIuser"--header"Content-TYpe:application/json"--requestPOST--data{} though the use of postman
and an evaluation script make for a more user friendly way to make and log sentiment predictions.

FastAPI can be run and tested using Postman Desktop locally. 
API includes 4 distinct endopints:
- Health Check (get): confirms that the API is running
- Predict sentiment (post): takes text & predicts sentiment
- Probability (post): takes input, outputs sentiment & proba
- training example (get): returns random dataset for testing
API logs prediction results to a json file with timestamp, review text, predicted sentiment and user-input true
sentiment. 

Streamlit Monitoring App is a dashboard service for viewing metrics.
This second container reads the logs from the shared volume to show
- Data Drift
- Target Drift analysis
- Model Accuracy & User Feedback
- Implementation Alert showing when calculated accuracy drops below 80%

Functionality includes an evaluate script, located in the root directory.
Successfully running this script uses Python requests library to run a test script to test and log 
movie reviews for analysis. Script loops through a provided json file with review text to analyze and
a user given sentiment to be properly logged in the log categories for app performance to be tracked
with the streamlit app.

