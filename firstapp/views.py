from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request):
    return HttpResponse("hello wellcome")

def show(request):
    return HttpResponse("hi vikky");

def send(request):
    http_resp = render(request,"index.html")
    return http_resp
def calculator(request):
    if request.method == "GET":
        return render(request,"calculator.html")


    if request.method == "POST":
        v1 = int(request.POST["t1"])
        v2 = int(request.POST["t2"])
        if "Add" in request.POST:
            res = v1+v2
            action ="addition"
        elif "Mul" in request.POST:
            res = v1*v2
            action="multiplication"
        elif "sub" in request.POST:
            res = v1-v2
            action="substraction"
        else:
            res = v1/v2
            action="division"
        return render(request, "calculator.html", {"result": res, "action": action})

def mtable(request):
    if request.method == "GET":
        return render(request,"mtable.html")

    if request.method == "POST":
        num =int(request.POST["t1"])
        output=[]
        for i in range(0,11):
            output.append(str(num)+"*"+str(i)+"="+str(i*num))
        return render(request,"mtable.html",{"result":output})