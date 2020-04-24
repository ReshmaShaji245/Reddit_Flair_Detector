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
  
  
The Jupyter Notebook Flair_Detector fetches the Reddit India Data using the praw module.
The Jupyter Notebook Model_Analysis_and_Evaluation selects that ML model with the best test accuracy, that is the Logistic Regression Model.

## Data Collection
  ~ The title,body and comments of the Reddit India posts were fetched using the praw module and were cleaned and combined together. This feature was used to train different models.
  
## Model selection
  ~ The collected dataset was used to train different Machine Learning Algorithms like KNN classification algorithm,Decision Tree classification Algorithm, SVM, and Logistic regression and analysis was done based on the accuracy scores of each. Logistic Regression gave the best accuracy score of 78%. Thus Logistic Regression was used selected and was used to predict the flair from the post URL.
  
  
