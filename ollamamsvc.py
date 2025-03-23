from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
import os
import logging
import ollama
import argparse
import sys

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set logging level to ERROR to suppress GET 
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # Default host and port
db = client['aichat']
collection = db['mycollection']

client = ollama.Client()

# Define a list of available models
models = ["deepseek-r1", "llama3.2","samantha-mistral", "falcon3", "codellama", "codestral","qwen2.5-coder:14B","olmo2"]

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Run the AI chat service.')
parser.add_argument('--model', type=str, choices=models, required=True, help='The AI model to use.')
args = parser.parse_args()

# Set the selected model
model = args.model
print(f"Using model: {model}")

def ai_generate(prompt):
    response = client.generate(model=model, prompt=prompt)
    return response.get('response', 'No response found')

@app.route('/documents', methods=['GET'])
def get_documents():
    documents = list(collection.find())
    for doc in documents:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
    return jsonify(documents)

@app.route('/documents', methods=['POST'])
def add_document():
    document = request.json
    document_id = collection.insert_one(document).inserted_id
    return jsonify(str(document_id))

@app.route('/documents/<id>', methods=['DELETE'])
def delete_document(id):
    result = collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Document deleted'}), 200
    else:
        return jsonify({'message': 'Document not found'}), 404

@app.route('/generate', methods=['POST'])
def generate_and_store():
    data = request.json

    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'message': 'Prompt is required'}), 400

    if prompt == '/bye':
        shutdown_server()
        return jsonify({'message': 'Server is shutting down...'}), 200

    response = ai_generate(prompt)
    document = {
        "query": prompt,
        "response": response,
    }
    document_id = collection.insert_one(document).inserted_id
    return jsonify({'id': str(document_id), 'response': response})

def shutdown_server():
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if shutdown:
        shutdown()
    else:
        print("Not running with the Werkzeug Server")
        sys.exit(1)

if __name__ == "__main__":
    app.run(debug=True, port=5001)