#!/usr/bin/env python
# coding: utf-8

# In[14]:


from pymongo import MongoClient
from bson.objectid import ObjectId

import json

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'BEE1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34065
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            check = self.database.animals.insert_one(data)  # data should be dictionary            
            if check != 0:
                return True
            return False
        
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, search):
        if search:
            data = list(self.database.animals.find(search, {"_id": False}))
        else:
            data = list(self.database.animals.find({}, {"_id": False}))
        
        return data
    
    def update(self, search, update):
        if search is not None:
            result = self.database.animals.update_many(search, {"$set": update})
        else:
            return "{}"
        
        return result.raw_result
    
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_many(data)
        else:
            return "{}"
        
        return result.raw_result


