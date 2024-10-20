from flask import Flask, render_template, request, jsonify
from tars import main_process
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')
  

@app.route('/process', methods=['POST'])
def process():
  data = request.get_json()  # Use get_json to parse the JSON data
  if data:
    query = data.get('query')
    # Call the main_process function to get a response
    response = main_process(query)  # Assuming main_process takes the user query as input
    return jsonify({'response': response})
  else:
    return jsonify({"error": "Missing query in request body"}), 400
  

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  
    app.run(host='0.0.0.0', port=port)
