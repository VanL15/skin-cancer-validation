from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def house(request):
    return render(request, "page2.html")
