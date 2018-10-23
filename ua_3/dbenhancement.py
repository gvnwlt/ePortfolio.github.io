#!/usr/bin/python
import json
from bson import json_util
from pymongo import MongoClient
import datetime
import string
from collections import OrderedDict
import bottle
from bottle import request, route, run, abort, response, post
import pickle

# set up URI paths for REST service

#---------------------------------------------------------------------------------
#  CRUD OPERATIONS
#---------------------------------------------------------------------------------
@route('/create', method='POST')
def insert_document():
  try:
    key = request.json.get("key")
    value = request.json.get("value")
    document = {key : value}
    connection = MongoClient('localhost', 27017)
    db = connection['market']
    collection = db['stocks']
    result=collection.save(document)
  except NameError as e:
    abort(400, str(e))
  return json.loads(json.dumps(document, indent=4, default=json_util.default))

@route('/read', method='GET')
def get_moving_average():
  try:
    low = request.query.low
    high = request.query.high
    connection = MongoClient('localhost', 27017)
    db = connection['market']
    collection = db['stocks']
    document = {"50-Day Simple Moving Average" : {'$gt' : int(low), '$lt' : int(high)}}
    result=collection.find_one(document)
  except ValidationError as ve:
		abort(400, str(ve))
  return json.loads(json.dumps(result, indent=4, default=json_util.default))

@route('/update')
def update():
  try:
    key = request.query.key
    value = request.query.value
    newValue = request.query.newValue
    connection = MongoClient('localhost', 27017)
    db = connection['market']
    collection = db['stocks']
    result=collection.update_one({key : value}, {"$set" : {key : newValue}})
  except :
    abort(400)
  return key

@route('/delete')
def delete_document():
  try:
    key = request.query.key
    value = request.query.value
    document = {key : value}
    connection = MongoClient('localhost', 27017)
    db = connection['market']
    collection = db['stocks']
    result=collection.delete_one(document)
  except ValidationError as ve:
    abort(400, str(ve))
  return document;

#---------------------------------------------------------------------------------
#  SPECIAL OPERATIONS
#---------------------------------------------------------------------------------

#  "Profit Margin", 
#  "Return on Assests", 
#  "Insider Transactions", 
#  "Short Ratio"    
#  
#  pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()

pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)

print(example_dict)
print(example_dict[3])

@route('/predict', method='GET')
def predict_profit_margin():
  try:
    company = request.query.company
    ra = "Return on Assets"
    it = "Insider Transactions"
    sr = "Short Ratio"
    connection = MongoClient('localhost', 27017)
    db = connection['market']
    collection = db['stocks']
    read = collection.find_one({"Company" : company}, {ra : 1, it : 1, sr : 1})
    sample = [[read['ra']], read['it'], read['sr']]
    withopen("regressionmodel.pickle", "rb") as modelfile:
      regression = pickle.load(modelfile)
    result = predict(sample)
  except ValidationError as ve:
		abort(400, str(ve))
  return result

@route('/stockSummary', method='GET')
def get_summary():
  try:
    ticker = request.query.ticker
    summary = request.query.summary
    connection = MongoClient('localhost', 27017)
    db = connection['market']
    collection = db['stocks']
    #document = {{"Ticker" : ticker}, {summary : 1}}
    result=collection.find_one({"Ticker" : ticker}, {summary :1})
  except ValidationError as ve:
		abort(400, str(ve))
  return json.loads(json.dumps(result, indent=4, default=json_util.default))

@route('/topFive', method='GET')
def get_top5():
  try:
    industry = request.query.industry
    connection = MongoClient('localhost', 27017)
    db = connection['market']
    collection = db['stocks']
    result=collection.find({"Industry" : industry})
  except ValidationError as ve:
		abort(400, str(ve))
  return json.loads(json.dumps(result, indent=4, default=json_util.default))



if __name__ == "__main__":
 #app.run(host='localhost', port=8080, debug=True)
 run(host='localhost', port=8080)
 
 