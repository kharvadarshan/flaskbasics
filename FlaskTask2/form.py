from flask import Flask,request, render_template
from dotenv import load_dotenv
import pymongo
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.test
collection = db['form-data']

app = Flask(__name__)

@app.route('/')
def home():
       return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submitForm():
      form_data = dict(request.form)
      collection.insert_one(form_data)
      print(form_data)
      return "Data submitted successfully"
      
if __name__ == '__main__':
    app.run(debug=True)