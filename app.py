from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import pickle

app = Flask(__name__)


@app.route('/')
def sentiment():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    cv = CountVectorizer()
    save_cv = open('model/cv_model.pkl', 'rb')
    cv_predict = pickle.load(save_cv)
    save_clf_model = open('model/clf_model.pkl', 'rb')

    clf_predict = pickle.load(save_clf_model)
    if request.method == 'POST':
        comment = request.form['textcomment']
        vect = cv_predict.transform([comment]).toarray()
        my_prediction = clf_predict.predict(vect)
    return render_template('result.html', prediction=my_prediction)


if __name__ == '__main__':
    app.run(debug=True)
  
