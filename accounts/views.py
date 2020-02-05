from django.contrib.auth.models import User
from django.shortcuts import render
# Create your views here.

# def register(request):
#     return render(request, 'register.html')

def login(request):
    return render(request, 'login-logout.html')

def registerUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user_type = request.POST['user_type']
        user = User.objects.create_user(username, "harsh", "jain", email, password, user_type, "9999999999", "surat", area_id=None)
        user.save()
        print("User Created")
        return render(request, '../index.html')
    else:
        return render(request, '../index.html')

