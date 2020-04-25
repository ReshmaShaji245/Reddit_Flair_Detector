# Reddit Flair Detector

This web application can predict the flairs of Reddit India posts using Machine Learning Algorithms.The application can be found on https://r-india-flair-detector.herokuapp.com
This is a Flask web application deployed on Heroku and the entire code is written in Python.

The directory Flair-Detector-Model contains all the necessarary files and folders for the Flask Web Application.
### app.py:
  ~This python file is used to start the Flask application.
  
### Requirements.txt:
  ~This file contains all the necessary dependancies.
  
### Templates: 
   ~This folder contains all the html templates.
   
### Data:
   ~This folder contains all the necessary datas for the app.
   
### Procfile:
  ~This file specifies the commands that are executed by the app on startup.
  
### Flair-detector.py:
  ~This file contains the Machine Learning Model that predicts the flair.
  
  
### Flair_Detector.ipynb:
~Reddit India Data was fetched here using the praw module.

### Model_Analysis_and_Evaluation.ipynb:
~This Jupyter Notebook was used to select that ML model with the best test accuracy score, that is the Logistic Regression Model.

### Reddit_data.csv: 
~Collected dataset.

## Data Collection
  ~ The title,body and comments of the Reddit India posts were fetched using the praw module and were cleaned and combined together. This feature was used to train different models.
  
## Model selection
  ~ The collected dataset was split into training(70%) and test data(30%). 
  
  ~The train data was used to train different Machine Learning Algorithms like KNN classification algorithm,Decision Tree classification Algorithm, SVM, and Logistic regression.
  
  ~Analysis was done based on the accuracy scores of each using the test data. 
  
  ~Logistic Regression gave the best accuracy score of 78.7%. 
  
  ~Thus Logistic Regression was selected and was used to predict the flair from the post URL.
  
  
