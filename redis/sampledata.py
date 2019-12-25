import uuid
import random
import string
from datetime import datetime

def genuuid():
    return str(uuid.uuid4())

def dateTime():
    return str(datetime.now())

def randomINT():
    return random.randint(0,10000000)

def randomIP():
    return random.randint(1, 0xffffffff)

def randomChar(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

sample = {
    "id": "RANDOM_ID",
    "ip": "RANDOM_IP",
    "port": "RANDOM_INT",
    "area_code": "RANDOM_INT",
    "longitude": "RANDOM_INT",
    "latitude": "RANDOM_INT",
    "timestamp": "TIME",
 }

def create_rand_data():
    test                = sample
    test['port']        = test['area_code'] = test['longitude'] = test['latitude'] = randomINT()
    test['ip']          = randomIP()
    test['timestamp']   = dateTime()
    test['id']          =  genuuid()
    return {genuuid():test}
