# from django.http import HttpResponse 
# if we dont send file, we will use HttpResponse("hello world")
# if we want to send file in slash (/) request we require or import render function

from django.shortcuts import render

def home(req):
    data = {"name" : "azhar"}
    
    return render(req,"index.html" ,data)

def fullname(request):
    fname = request.get.Get('firstname')
    lname = request.Get.Get('lastname')

    fullname = f"{fname} {lname}"
    data = {"fullname" : fullname}
    return render(request , "index.html" , fullname)