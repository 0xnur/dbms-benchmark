from pymongo import MongoClient
'''
Get keys from mongodb for update and select
'''
def mongoKeys():
    mongo_client = MongoClient()
    db = mongo_client.hacettepe
    col = db.test
    return col.distinct('_id')
