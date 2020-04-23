import pandas as pd
import numpy as np
df=pd.read_csv(r"c:\Users\alres\Downloads\reddit_data.csv")
df.head()
X=df['0']
Y=df['1']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state = 1)
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression


lr = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()), ('clf', LogisticRegression(n_jobs=1, C=1e5))])
lr.fit(X_train, y_train)
from sklearn.metrics import accuracy_score
log_pred=lr.predict(X_test)
print(log_pred)
acc4=accuracy_score(log_pred, y_test)
