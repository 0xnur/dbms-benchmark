from multiprocessing import Process, Event,Pool
import os
import time
import random
import argparse
import sys
from datetime import datetime
import uuid
import random
import string
from sampledata import *

def task(line):
    proc_id = os.getpid()
    f = open('output/same_file','w')
    for i in range(int(line)):
        f.write(str(create_rand_data())+"\n")
    #print('timestamp of process id {}: {}'.format(proc_id, time.time()))
    f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Writing test script. Write output to files by using multiple async process.')
    parser.add_argument('-p', dest='process_count', type=int, help='async process count')
    parser.add_argument('-l', dest='line',type=int, help='random data line count')
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
