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
Test: Update counts (how many update?)
Keys: Mongo keys list
'''
def task(test,keys):
    try:
        mongo_client = MongoClient()
        db = mongo_client.hacettepe
        col = db.test
        for i in range(int(test)):
            col.replace_one({'_id': random.choice(keys)},  create_rand_data())
        mongo_client.close()
    except Exception as e:
        print e.message, e.args

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Writing test script. Write output to files by using multiple async process.')
    parser.add_argument('-p', dest='process_count', type=int, help='async process count')
    parser.add_argument('-l', dest='line',type=int, help='update count')
    args = parser.parse_args()
    if len(sys.argv) == 1 or args.process_count is None or args.line is None:
        parser.print_help()
        sys.exit('give process number (-p) and line size (-l) as 2 different parameter: example -p 1000 -l 10')
    pool = Pool(processes=args.process_count)
    keys = mongoKeys()
    start_time = time.time()
    [pool.apply_async(task, args=(args.line,keys)) for i in range(args.process_count)]
    pool.close()
    pool.join()
    print("--- %s seconds ---" % (time.time() - start_time))
