import redis as R
'''
Get redis keys from DB to select and update tests
'''
def redisKeys():
    r = R.Redis(host='localhost', port=6379, db=0)
    return r.keys()
