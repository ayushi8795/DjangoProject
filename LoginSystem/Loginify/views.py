from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from .models import User as userDetails
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the Loginify index.")
@csrf_exempt
def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not userDetails.objects.filter(email =email).exists():
            userDetails.objects.create(username=username, email=email, password=password)
            return redirect('login')
        else:
            return render(request, 'signup.html', {'error': 'Email already registered'})
    return render(request, 'signup.html')
@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = userDetails.objects.get(email=email, password=password)
            return render(request, 'success.html')
        except userDetails.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
@csrf_exempt
def getAllUsers(request):
    users = userDetails.objects.all()
    
    return JsonResponse(list(users.values()), safe=False)
@csrf_exempt
def userByEmail(request, email):
    try:
        user = userDetails.objects.get(email=email)
        return HttpResponse(user)
    except userDetails.DoesNotExist:
        return HttpResponse("User not found.")

@csrf_exempt
def deleteUser(request, email):
    try:
        user = userDetails.objects.get(email=email)
        user.delete()
        return HttpResponse("User deleted successfully.")
    except userDetails.DoesNotExist:
        return HttpResponse("User not found.")
    
@csrf_exempt
def updateUser(request, email):
    if request.method == 'PATCH':
        try:
            user = userDetails.objects.get(email=email)
            user.username = request.POST.get('username', user.username)
            user.password = request.POST.get('password', user.password)
            user.save()
            return HttpResponse("User updated successfully.")
        except userDetails.DoesNotExist:
            return HttpResponse("User not found.")
    return render(request, 'update_user.html', {'email': email})