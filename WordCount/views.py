import pymongo
import pandas as pd
from django.contrib.sites import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# This method will be executed when the home page starts
from django.template import loader
from django.urls import reverse


def home(request):
    db_list = connect()
    list1 = db_list[0]
    list2 = db_list[1]
    list3 = db_list[2]
    list4 = db_list[3]

    all_final_list = []
    for i in range(0, len(list1)):
        new_list = []
        new_list.append(list1[i])
        new_list.append(list2[i])
        new_list.append(list3[i])
        new_list.append(list4[i])
        all_final_list.append(new_list)

    return render(request, 'home.html',
                  {'final_all': all_final_list})


# The Edit Function
def edit(request):
    if request.method == 'POST':
        if '+' in request.POST.values():
            pair = [key for key in request.POST.keys()][1].split("|")
            print(pair)

    return render(request, 'edit.html', {'to_edit_list': pair})


def submitEdit(request):
    client = pymongo.MongoClient(
        "mongodb+srv://Cluster012345:Cluster012345@cluster0-zu94n.gcp.mongodb.net/test?retryWrites=true&w=majority")

    db = client.get_database('test')
    records = db.employees

    if request.method == 'POST':
        name = request.POST.get('name')
        country = request.POST.get('country')
        profession = request.POST.get('profession')

        print(name + "   ,   " + country)

        employee_update = {
            'country': country,
            'profession': profession
        }

        records.update_one({'name': name}, {'$set': employee_update})
        #
        db_list = connect()
        list1 = db_list[0]
        list2 = db_list[1]
        list3 = db_list[2]
        list4 = db_list[3]

        all_final_list = []
        for i in range(0, len(list1)):
            new_list = []
            new_list.append(list1[i])
            new_list.append(list2[i])
            new_list.append(list3[i])
            new_list.append(list4[i])
            all_final_list.append(new_list)
        #
        return render(request, 'home.html', {'final_all': all_final_list})
        # return HttpResponse('home.html')


def delete(request):
    client = pymongo.MongoClient(
        "mongodb+srv://Cluster012345:Cluster012345@cluster0-zu94n.gcp.mongodb.net/test?retryWrites=true&w=majority")

    db = client.get_database('test')
    records = db.employees

    if request.method == 'POST':
        if '+' in request.POST.values():
            pair = [key for key in request.POST.keys()][1].split("|")
            print(pair)

    records.delete_one({'name': pair[0]})

    #
    db_list = connect()
    list1 = db_list[0]
    list2 = db_list[1]
    list3 = db_list[2]
    list4 = db_list[3]

    all_final_list = []
    for i in range(0, len(list1)):
        new_list = []
        new_list.append(list1[i])
        new_list.append(list2[i])
        new_list.append(list3[i])
        new_list.append(list4[i])
        all_final_list.append(new_list)
    #
    return render(request, 'home.html', {'final_all': all_final_list})


def addEmployee(request):
    return render(request, 'addEmployee.html')


def submitAddEmployee(request):
    client = pymongo.MongoClient(
        "mongodb+srv://Cluster012345:Cluster012345@cluster0-zu94n.gcp.mongodb.net/test?retryWrites=true&w=majority")

    db = client.get_database('test')
    records = db.employees
    mydb = client["test"]
    myCol = mydb["employees"]
    df = pd.DataFrame(myCol.find())

    dataframeSize = len(df)
    list_name = []
    for i in range(0, dataframeSize):
        list_name.append(df['name'][i])

    if request.method == 'POST':
        name = request.POST.get('name')
        country = request.POST.get('country')
        profession = request.POST.get('profession')
        email = request.POST.get('email')

    if name in list_name:
        print("Name Already exist")
    else:
        new_employee = {
            'name': name,
            'country': country,
            'profession': profession,
            'email': email
        }
        records.insert_one(new_employee)

        #
        db_list = connect()
        list1 = db_list[0]
        list2 = db_list[1]
        list3 = db_list[2]
        list4 = db_list[3]

        all_final_list = []
        for i in range(0, len(list1)):
            new_list = []
            new_list.append(list1[i])
            new_list.append(list2[i])
            new_list.append(list3[i])
            new_list.append(list4[i])
            all_final_list.append(new_list)
        #

    return render(request, 'home.html', {'final_all': all_final_list})


# Retrieving data from Database
def connect():
    client = pymongo.MongoClient(
        "mongodb+srv://ahsan:ahsan@cluster0-zu94n.gcp.mongodb.net/test?retryWrites=true&w=majority")
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
