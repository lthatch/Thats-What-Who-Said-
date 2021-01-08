from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import joblib

app = Flask(__name__)
model = joblib.load('../models/search.pkl')
count = CountVectorizer(lowercase=True, decode_error="replace",vocabulary=joblib.load('../models/searchcountVec.pkl'))
tfidf = TfidfTransformer()


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    text = str(request.form['Input'])
    text = [text]
    countvec = count.transform(text)
    text_tfidf = tfidf.fit_transform(countvec)
    prediction = model.predict(text_tfidf)

    for i in prediction:
        pred = i

    if pred == 'Michael':
        image = '../static/images/michael.jpg'
    elif pred == 'Jim':
        image = '../static/images/jim.jpg'
    elif pred == 'Dwight':
        image = '../static/images/dwight.jpg' 
    elif pred == 'Andy':
        image = '../static/images/andy.jpg'
    elif pred == 'Angela':
        image = '../static/images/angela.jpg'
    elif pred == 'Creed':
        image = '../static/images/creed.png'
    elif pred == 'Darryl':
        image = '../static/images/darryl.jpg'
    elif pred == 'Kevin':
        image = '../static/images/kevin.jpeg'
    elif pred == 'Pam':
        image = '../static/images/pam.jpg'
    elif pred == 'Stanley':
        image = '../static/images/stanley.jpg'
    
    return render_template('result.html', prediction_text=pred, image=image)

if __name__=="__main__":
    app.run(debug=True)