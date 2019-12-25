from multiprocessing import Process, Event,Pool
import os
import time
import redis as R
import random
import argparse
from datetime import datetime
from sampledata import *
from redis_keys import *
import sys


'''
Test: Update counts (how many update?)
Keys: Redis keys list
'''
def task(test,keys):
    try:
        r = R.Redis(host='localhost', port=6379, db=0)
        pipe = r.pipeline()
        for i in range(int(test)):
            data = create_rand_data()
            values = create_rand_data().values()[0]
            r.hmset(random.choice(keys),values)
        pipe.execute()
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
    keys = redisKeys()
    start_time = time.time()
    [pool.apply_async(task, args=(args.line,keys)) for i in range(args.process_count)]
    pool.close()
    pool.join()
    print("--- %s seconds ---" % (time.time() - start_time))
