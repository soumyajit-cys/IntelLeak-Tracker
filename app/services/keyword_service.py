from app.database.mongodb import keyword_collection

def add_keyword(value):
    return keyword_collection.insert_one({"value": value})

def get_keywords():
    return list(keyword_collection.find({}, {"_id": 0}))

def delete_keyword(value):
    return keyword_collection.delete_one({"value": value})