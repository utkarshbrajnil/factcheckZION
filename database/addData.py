# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
from pymongo import MongoClient

client=MongoClient('localhost',27017)
db=client['ZION']
coll=db['user_info']

with open('factcheckZION/database/user.json') as f:
    data=json.load(f)

coll.insert_many(data)

client.close()

print("completed")
