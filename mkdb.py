from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # Default host and port
# Drop the existing database if it exists
client.drop_database('aichat')

db = client['aichat']
collection = db['mycollection']

# Insert a document
document = {
    "query": "Sample AI query",
    "response": "Sample AI response",
}

result = collection.insert_one(document)
print(f"Inserted document with _id: {result.inserted_id}")

# Query documents
documents = collection.find()
for doc in documents:
    print(doc)