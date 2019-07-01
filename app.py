from flask import Flask,request,jsonify,abort
from sklearn.externals import joblib

classifier=joblib.load('classifier.pkl')
vectorizer=joblib.load('vectorizer.pkl')


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/predict', methods=['POST'])
def create_task():
    print(request.json)
    
        
    return jsonify({'prediction':int(classifier.predict(vectorizer.transform([request.json['tweet']]).toarray()))}), 201

if __name__ == '__main__':
    app.run(debug=False)


