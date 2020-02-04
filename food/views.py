import os
from django.shortcuts import render

# Create your views here.


def index(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_path = os.path.join(BASE_DIR, 'bootstrap')
    params = {'dir': base_path}
    return render(request, 'food/index.html', params)


