from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    df = pd.read_csv("YoutubeSpamMergedData.csv")
    df_data = df[["CONTENT", "CLASS"]]
    # Features and Labels
    df_x = df_data["CONTENT"]
    df_y = df_data.CLASS
    # Extract Feature With CountVectorizer
    corpus = df_x
    cv = CountVectorizer()
    X = cv.fit_transform(corpus)  # Fit the Data
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        X, df_y, test_size=0.33, random_state=42
    )
    # Naive Bayes Classifier
    from sklearn.naive_bayes import MultinomialNB

    model_clf = MultinomialNB()
    model_clf.fit(X_train, y_train)
    print(model_clf.score(X_test, y_test))
    # Alternative Usage of Saved Model
    filename = 'model_clf.pkl'
    joblib.dump(model_clf, filename)
    
    # some time later...
    
    # load the model from disk
    loaded_model = joblib.load(filename) 
    print("Loaded model: ",loaded_model.score(X_test, y_test))

    if request.method == "POST":
        comment = request.form["comment"]
        data = [comment]
        vect = cv.transform(data).toarray()
        my_prediction = loaded_model.predict(vect)
    return render_template("result.html", prediction=my_prediction)


if __name__ == "__main__":
    app.run(debug=True)
