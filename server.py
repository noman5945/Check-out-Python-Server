from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv,find_dotenv
import os

load_dotenv(find_dotenv())
#Get password fron .env file
password=os.environ.get("MONGODB_PWD")

#connect to the database and get the client(cluster)
connection_string= f"mongodb+srv://abdullahnoman5945:{password}@cluster0.rqebvmt.mongodb.net/?retryWrites=true&w=majority"
client=MongoClient(connection_string)

#after connection get the database
database=client.Checkout

#after getting the database get a "Collection"(Table) here we take the "restaurant" collection of "Checkout database"
restaurant_collection=database.restaurants


#Inside "restaurant" collection the "document"(data) will be stored in this format
rest_data_struct=[
    {
    "name": "Kudos",
    "img": "https://img.freepik.com/free-photo/double-hamburger-isolated-white-background-fresh-burger-fast-food-with-beef-cream-cheese_90220-1192.jpg",
    "ratings": "4.7",
    "opening": "10:00am",
    "closing": "08:00pm",
    "WorkTime": "Day",
    "lowestPrice": 350,
    "highestPrice":1300,
    "features":["Open Space","Rooftop","Offers"],
    "mainFoods":["Burger","Fries","Shakes"],
    "location":"Mohammedpur"
    },
    {
    "name": "TakeOut",
    "img": "https://img.freepik.com/free-photo/double-hamburger-isolated-white-background-fresh-burger-fast-food-with-beef-cream-cheese_90220-1192.jpg",
    "ratings": "4.7",
    "opening": "10:00am",
    "closing": "08:00pm",
    "WorkTime": "Day",
    "lowestPrice": 450,
    "highestPrice":1300,
    "features":["Open Space","Rooftop","Live Concert"],
    "mainFoods":["Burger","Fries","Shakes","Nuggets","Shawrma"],
    "location":"Mohammedpur"
    },
    {
    "name": "Cheapy",
    "img": "https://img.freepik.com/free-photo/double-hamburger-isolated-white-background-fresh-burger-fast-food-with-beef-cream-cheese_90220-1192.jpg",
    "ratings": "4.7",
    "opening": "10:00am",
    "closing": "08:00pm",
    "WorkTime": "Day",
    "lowestPrice": 200,
    "highestPrice":1300,
    "features":["Open Space","Rooftop","Live Concert"],
    "mainFoods":["Burger","Fries","Shakes","Nachos"],
    "location":"Mohammedpur"
    },
    {
    "name": "Burger Express",
    "img": "https://img.freepik.com/free-photo/double-hamburger-isolated-white-background-fresh-burger-fast-food-with-beef-cream-cheese_90220-1192.jpg",
    "ratings": "4.7",
    "opening": "10:00am",
    "closing": "08:00pm",
    "WorkTime": "Day",
    "lowestPrice": 400,
    "highestPrice":1800,
    "features":["Open Space","Rooftop","Live Concert"],
    "mainFoods":["Burger","Fries","Shakes","Nachos"],
    "location":"Mohammedpur"
    }
  ]

#These are functions which performs some querys
def insert_one_restaurent(data):
    
    insertedID=restaurant_collection.insert_one(data).inserted_id
    print(insertedID)

def insert_many_restaurents(data):
    result=restaurant_collection.insert_many(data)
    print(result.inserted_ids)


def search_rest_by_location(location):
    rests=restaurant_collection.find({"location":location})
    list_of_rests=list(rests)
    print(list_of_rests)

def search_rest_by_name(name):
    rests=restaurant_collection.find({"name":name})
    list_of_rests=list(rests)
    print(list_of_rests)

#This function searches and gives data given the price range location and the food keys 
def search_by_location_price(loc,lowprice,highprice,food_keys):
    query={"location":loc,
        "lowestPrice":{'$lte':lowprice},
        "highestPrice":{'$gte':highprice},
        "mainFoods":{'$in':food_keys}
        }
    rests=restaurant_collection.find(query)
    
    list_of_rests=list(rests)
    printLists(list_of_rests)

def printLists(rests):
    for rest in rests:
        print(rest['name'])
#Inserting Restaurants
#insert_one_restaurent(rest_data_struct)
#insert_many_restaurents(rest_data_struct)

#Searching
#search_rest_by_name("Takeout")
#search_rest_by_location("Gulshan")
search_by_location_price("Dhanmondi",450,600,["Shakes"])