# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 20:49:43 2020

@author: alres
"""


import sklearn
import re
from praw.models import MoreComments
import itertools
from bs4 import BeautifulSoup
import nltk
#nltk.download('all')
from nltk.corpus import stopwords
import flask
import pandas as pd
from flask import Flask,request,render_template,url_for,send_file
import json
import os
import praw
from Flair_detector import lr

reddit=praw.Reddit(client_id='acP3HQrR6pmNDQ',client_secret='9Ii4t82UOtuwc9ADN4Dv_j3hL6E',user_agent='Flair_detector',username='OmegaDeathOmega',password='omegaDeath_')
UPLOAD_FOLDER = '\Downloads'

REPLACE_BY_SPACE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))
def clean_text(text):
   
             text = BeautifulSoup(text, "lxml").text
             text = text.lower()
             text = REPLACE_BY_SPACE.sub(' ', text)
             text = BAD_SYMBOLS.sub('', text)
             text = ' '.join(word for word in text.split() if word not in STOPWORDS)
             print(text)
             return text

global urls
urls=[]
data=[]

# app
app = flask.Flask(__name__,template_folder='templates')

# routes


@app.route('/predict',methods=['GET','POST'])

def predict():
     if flask.request.method=='GET':
         return flask.render_template('home.html')
     if flask.request.method=='POST':
         val = flask.request.form['url']   
         
         submission = reddit.submission(url=val)
         
         body=submission.selftext
         title=submission.title
         comments=[]
         for com in submission.comments:
             if isinstance(com, MoreComments):
                 continue
             comments.append(com.body)
         
         post_text=title+' '+body+' '+' '.join(comments)
         post_text=clean_text(post_text)
         df=[post_text]
         
     
         return flask.render_template("result.html",prediction=lr.predict(df))

dictionary={}        
@app.route('/automated_testing',methods=['GET','POST'])
def automated_testing():
     if flask.request.method=='GET':
          return flask.render_template('home.html')
     if flask.request.method=='POST':
          if 'file' not in flask.request.files:
               print('File not uploaded')
               return
          file=flask.request.files['file']
          file.save(os.path.join("data", file.filename))
          
          fp=open("data/"+file.filename,"r")

          
          

          for line in fp:
             strip_line=line.strip()
             urls.append(strip_line)
          
         
          return flask.render_template("downloads.html")

@app.route('/linking')
def linking():
    return render_template("automated_testing.html")

@app.route('/linking_home')
def linking_home():
    return render_template("home.html")



@app.route('/return-file')
def return_file():
    
    for line in urls:
          submission = reddit.submission(url=line)

          body=submission.selftext
          title=submission.title
          comments=[]
          for com in submission.comments:
              if isinstance(com, MoreComments):
                  continue
              comments.append(com.body)
         
          post_text=title+' '+body+' '+' '.join(comments)
          post_text=clean_text(post_text)
          data.append(post_text)
          
          
          
    
    lr_pred=lr.predict(data)
    for (i,j) in itertools.zip_longest(urls,lr_pred):
            dictionary[i]=j
          
    with open('pred.json','w') as fp:
         json.dump(dictionary,fp)

    return send_file('pred.json')


if __name__ == '__main__':
    app.run(port = 8000, debug=True)
    
    
    
