from multiprocessing import Process, Event,Pool
import os
import time
from pymongo import MongoClient
import random
import argparse
from datetime import datetime
from sampledata import *
from mongo_keys import *
import sys


'''
Test: Select counts
Keys: Mongo keys list
'''
def task(test,keys):
    try:
        mongo_client = MongoClient()
        db = mongo_client.hacettepe
        col = db.test
        for i in range(int(test)):
            col.find_one({'_id': random.choice(keys)})
        mongo_client.close()
    except Exception as e:
        print e.message, e.args

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test scripts.')
    parser.add_argument('-p', dest='process_count', type=int, help='give process number')
    parser.add_argument('-l', dest='line',type=int, help='select count')
    args = parser.parse_args()
    if args.process_count == '' and args.line == '':
        sys.exit('give process number (-p) and line size (-l) as 2 different parameter: example -p 1000 -l 10')
    pool = Pool(processes=args.process_count)
    keys = mongoKeys()
    keys = mongoKeys()
    start_time = time.time()
    [pool.apply_async(task, args=(args.line,keys)) for i in range(args.process_count)]
    pool.close()
    pool.join()


print("--- %s seconds ---" % (time.time() - start_time))
