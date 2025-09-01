from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def myapp(request):
#     return HttpResponse("hello Django")

def success_page(request):
    return HttpResponse("<h1>hello</h1>")

def myapp(request):
    peoples=[
        {'name':'rohit','age':20},
        {'name':'rahul','age':16},
    ]
    return render(request,"index.html",context={'peoples':peoples})


def myapp(request):
    persons=[
        {'name':'diya','age':30},
        {'name':'vansh','age':14},
        {'name':'riya','age':40},
        {'name':'vira','age':84},
        {'name':'nensi','age':32},
        {'name':'vanshika','age':64},
        {'name':'dhyan','age':12},
        {'name':'dhenu','age':14},
        {'name':'maitri','age':50},
        {'name':'rudra','age':11},
        {'name':'manav','age':9},
        {'name':'mansi','age':14},
        {'name':'yatri','age':57},
        {'name':'vansh','age':19},
        {'name':'diya','age':7},
        {'name':'rena','age':3},
        {'name':'mira','age':55},
        {'name':'kruti','age':12},
        {'name':'nijal','age':63},
        {'name':'ishika','age':32},
        {'name':'rohit','age':22}

        

    ]
    return render(request,"myindex1.html",context={'persons':persons})

