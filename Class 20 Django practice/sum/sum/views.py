from django.shortcuts import render

def index(request):
    return render(request,('index.html'))


def total(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operator = request.GET.get('operator')
    total = 0
    print(num1,num2,operator)
    if (operator == '*'):
        total = int(num1) * int(num2)
    elif (operator == '+'):
        total = int(num1) + int(num2)
    elif (operator == '-'):
        total = int(num1) - int(num2)
    elif (operator == '/'):
        total = int(num1) / int(num2)
    else:
        total = 'haha'
        
    dic = {"total" : total}
    return render(request,'total.html' ,dic)
 

