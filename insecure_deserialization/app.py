from flask import Flask, request
import pickle


app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the insecure deserialization demo!'


@app.route('/load', methods=['POST'])
def load_data():
    data = request.data
    obj = pickle.loads(data)
    return f'Deserialized object: {obj}'



if __name__ == '__main__':
    app.run(debug=True)
