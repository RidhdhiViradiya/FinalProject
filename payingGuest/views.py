from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'payingGuest/index.html')

def addrooms(request):
    return render(request, 'payingGuest/addrooms.html')


