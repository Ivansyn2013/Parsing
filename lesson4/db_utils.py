from pymongo import MongoClient

def init_db_session():
    client = MongoClient("mongodb://root:example@0.0.0.0:22222/")
    db = client['vacations']
    session = db['vacations']
    return session