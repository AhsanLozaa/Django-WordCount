import pymongo
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render


# This method will be executed when the home page starts
def home(request):
    db_list = connect()
    list1 = db_list[0]
    list2 = db_list[1]
    list3 = db_list[2]
    list4 = db_list[3]

    all_final_list = []
    for i in range(0, 4):
        new_list = []
        new_list.append(list1[i])
        new_list.append(list2[i])
        new_list.append(list3[i])
        new_list.append(list4[i])
        all_final_list.append(new_list)

    return render(request, 'home.html',
                  {'final_all': all_final_list})


def eggs(request):
    return HttpResponse("<h1>Hello, eggs are great</h1>")


def connect():
    client = pymongo.MongoClient(
        "mongodb+srv://Cluster012345:Cluster012345@cluster0-zu94n.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test

    mydb = client["test"]
    myCol = mydb["employees"]
    df = pd.DataFrame(myCol.find())

    dataframeSize = len(df)
    list_name = []
    list_country = []
    list_profession = []
    list_email = []
    for i in range(0, dataframeSize):
        list_name.append(df['name'][i])
        list_country.append(df['country'][i])
        list_profession.append(df['profession'][i])
        list_email.append(df['email'][i])

    final_list = []
    final_list.append(list_name)
    final_list.append(list_country)
    final_list.append(list_profession)
    final_list.append(list_email)

    return final_list
