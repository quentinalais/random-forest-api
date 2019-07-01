from flask import Flask
from sklearn.externals import joblib
classifier=joblib.load('classifier.pkl')

vectorizer=joblib.load('vectorizer.pkl')


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/predict', methods=['POST'])
def create_task():
    if not request.json or not 'tweet' in request.json:
        abort(400)
    task = {
        
        'prediction': classifier.predict(vectorizer.transform([request.json['tweet']]).toarray())
      
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True)


