import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline, FeatureUnion

import pickle

app = Flask(__name__)
model = pickle.load(open('MSA.pkl', 'rb'))
un = pickle.load(open('union.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    sent2 = union.transform(final_features)

    prediction = model.predict(sent2)

    
    return render_template('index.html', prediction_text=prediction)


if __name__ == "__main__":
    app.run(debug=True)
