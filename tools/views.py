from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import  functionality_0
from .models import Rng, Fags, Found_in
from .forms import Array_limits, Fags_search, Fags_add
import random
import math



def base_func(response):
    return render(response, "tools/base.html")



def fags_home(response):
    all_fags = Fags.objects.all()
    print(all_fags)
    length = len(all_fags)
    return render(response, "tools/fags_home.html", {"fags":all_fags, "len": length})
    # remains for next session .
    # you need to pass len of all_fags to the frontend where there will be a list of
    # links to the individual fags in hyperlink like 
    # <a href="http://127.0.0.1:8000/{{i}}">
    # {{i}} being the i in loop which will run for len times  

def individual_fags(response,fag):
    product = Fags.objects.get(fag = fag)
    product_id = product.fag.replace("_", " ").title()
    product_price = product.price
    product_switch = product.switch
    cities = []
    product_availabilty = product.found_in_set
    for i in range(len(product_availabilty.all())):
        cities.append(product_availabilty.get(id=i+1).city)
    
    print(cities)
    # <QuerySet [<Found_in: dhaka>]>

    return render(response, "tools/individual_fags.html", {"context":{"product_id":product_id, "product_price":product_price, "product_switch":product_switch},"cities":cities})

def fags_search(response):
    form = Fags_search(response.POST or None)
    product_id = None
    product_price = None
    product_switch = None
    if response.method == "POST":
        if form.is_valid():
            fag = form.cleaned_data["fag"]
            # database_search = Fags.objects.filter(fag__startswith=fag[0:1])
            product_id = Fags.objects.get(fag=fag)
            # product_id = product_id.replace("_", " ").title()
            product_price = Fags.objects.get(fag=fag).price
            product_switch = Fags.objects.get(fag=fag).switch
    return render(response, "tools/fags_search.html", {"form":form, "context":{"product_id":product_id, "product_price":product_price, "product_switch":product_switch} })
        
    
    

def fags_add(response):
    # returned from response.POST
    # <QueryDict: {'csrfmiddlewaretoken': ['Fpaz2nzDO7mAc1KHGsOzUx1KmqIzWaqnat17QHSUYxkkYaaj23agqR8KQA2NAp9v'],
    #              'fag': ['benson_regular'], 'price': ['18'], 'switch': ['on'], 'save': ['']}>
    all_cities = ["dhaka","chattogram","khulna","rajshahi","mymensingh","cumilla","barishal","rangpur"]
    message = "Enter fag name and price to create a new to database. Switch is optional."
    if response.method == "POST":
        print(response.POST)
        form = Fags_add(response.POST)
        if form.is_valid():
            print(form.cleaned_data)
            fag = form.cleaned_data["fag"].lower()
            price = form.cleaned_data["price"]
            switch = form.cleaned_data["switch"]
            # print(fag, price, switch)
            try:
                fetched_fag = Fags.objects.get(fag=fag).fag
            except:
                fetched_fag = None
            # print(fetched_fag)
            if fetched_fag==None or fetched_fag.lower()!=fag:
                l= Fags(fag=fag,price=price,switch=switch)
                l.save()
                message = "added successfully"
            else:
                message = "couldnt add. duplicate was found"
            # print(message)
        else:
            message = "Invalid form.Nothing was added."
    else:
        form = Fags_add(None)
    return render(response, "tools/fags_add.html",{"title" : "Add Fags", "form": form, "message" : message,"all_cities":all_cities})
    




def rng(request,lower_limit=0, upper_limit=100, n=10):
    array = []
    form = Array_limits(request.POST or None)
    if request.method=="POST":
         
        if form.is_valid():
            lower_limit = form.cleaned_data["lower_limit"]
            upper_limit = form.cleaned_data["upper_limit"]
            n = form.cleaned_data["n"]
            for i in range(n):
                array.append(random.randint(lower_limit, upper_limit))
            array_query = Rng.objects.all()
            found = False

            l = Rng(array = array)
            l.save()
    return render(request, "tools/rng.html", {"context":array, "form" : form})    

    

# def rng(lower_limit=0, upper_limit=100, n=10):
#     array = []
#     distribution = []
#     limits = []
    
#     # initiating 0's
#     for i in range(10):
#         distribution.append(0)
#     # print("distribution", distribution)
    
    
    
#     if (upper_limit%100 != 0) and upper_limit>10 :
#         chunk_value = math.ceil(upper_limit/10)
#         temp_upper_limit = chunk_value*10
    
#         print("\n\n\nlower_limit", lower_limit, "\nupper_limit", upper_limit, "\nchunk_value",chunk_value,"\ntemp_upper_limit", temp_upper_limit,"\n\n\n")
    
#         for i in range(0,10):
#             limits.append((temp_upper_limit/10)*i)
#         print(limits)
#         for i in range(0,len(limits)-1):
#             print(i)
#             limits[i] = f"{str((limits[i])+1)}-{str(limits[i+1])}"
#         limits.pop()
#         print(limits)
