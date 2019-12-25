from multiprocessing import Process, Event,Pool
import os
import time
import redis as R
import random
import argparse
from datetime import datetime
from sampledata import *
import sys

'''
test: how many insert per process?
'''
def task(test):
    try:
        r = R.Redis(host='localhost', port=6379, db=0)
        for i in range(int(test)):
            data = create_rand_data()
            values = create_rand_data().values()[0]
            keys = create_rand_data().keys()[0]
            r.hmset(keys,values)
    except Exception as e:
        print e.message, e.args


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Writing test script. Write output to files by using multiple async process.')
    parser.add_argument('-p', dest='process_count', type=int, help='async process count')
    parser.add_argument('-l', dest='line',type=int, help='insert line count')
    args = parser.parse_args()
    if len(sys.argv) == 1 or args.process_count is None or args.line is None:
        parser.print_help()
        sys.exit('give process number (-p) and line size (-l) as 2 different parameter: example -p 1000 -l 10')
    pool = Pool(processes=args.process_count)
    start_time = time.time()
    #async process pool
    [pool.apply_async(task, args=(args.line,)) for i in range(args.process_count)]
    pool.close()
    pool.join()
    print("--- %s seconds ---" % (time.time() - start_time))
