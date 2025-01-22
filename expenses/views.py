from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'Expenses/index.html')



def add_expense(request):
    return render(request,'Expenses/add_exepense.html')