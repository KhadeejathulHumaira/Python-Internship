import json
x={
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "TakenTest":True,
    "average":67.99

},{
    "firstName" : "Rosh",
    "lastName" : "Vartin",
    "hobbies" : ["running", "Drawing", "dancing"],
    "age" : 39,
    "TakenTest":True,
    "average":66.99
}
with open("doc.json","w") as f:
    json.dump(x,f,indent=4)


from pymongo import MongoClient
myclient=MongoClient("mongodb://localhost:27017/")
db=myclient["mongdb"]
Collection=db["info"]
with open("doc.json") as f:
    data=json.load(f)
if isinstance(data,list):
    Collection.insert_many(data)
else:
    Collection.insert_one(data)
