from django.shortcuts import render

def index(request):
    return render(request,('index.html'))


def total(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    total = int(num1) + int(num2)
    dic = {"total" : total}
    return render(request,'total.html' ,dic)
 

