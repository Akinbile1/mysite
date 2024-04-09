from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
def index(request):
    return render(request, "authentication/index.html")

def signup(request):
    return render(request, "authentication/signup.html")
    
def signin(request):
    return render(request, "authentication/signin.html")

def forgotPass(request):
    return render(request, "authentication/forgotPass.html")

def logout_view(request):
    logout(request)
    return redirect('signin')  # Redirect to the login page or another appropriate page



def student_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordConf = request.POST.get('passwordConf')
        grade = request.POST.get('SchoolYear')
        subject = request.POST.get('CodingLanguage')

        if password != passwordConf:
            return HttpResponse("Passwords do not match", status=400)
        
        try:

            user = CustomUser.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=make_password(password)
            )

            Student.objects.create(
                user=user,
                grade=grade,
                subject=subject
            )

            login(request, user)
            return redirect('index')  # Redirect to a home page or another appropriate page
        except Exception as e:
            return HttpResponse(f"Failed : {e}")

    return render(request, 'authentication/student_signup.html')


def tutor_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        qualification = request.POST.get('qualification')
        subject = request.POST.get('subject')
        password = request.POST.get('password')
        passwordConf = request.POST.get('passwordConf')

        if password != passwordConf:
            return HttpResponse("Passwords do not match", status=400)

        user = CustomUser.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )

        Tutor.objects.create(
            user=user,
            qualification=qualification,
            subject=subject
        )

        login(request, user)
        return redirect('home')  # Redirect to a home page or another appropriate page

    return render(request, 'authentication/tutor_signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("logged in")
            # Check if the user is a tutor
            if hasattr(user, 'tutor_profile'):
                return redirect('tutor_dashboard')
            # Check if the user is a student
            elif hasattr(user, 'student_profile'):
                return redirect('student_dashboard')
        else:
            # Invalid login
            return HttpResponse("Passwords do not match", status=400)
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'authentication/signin.html')

@login_required(login_url='/signin/')
def tutor_dashboard(request):
    return render(request, 'authentication/tutor_dashboard.html')

@login_required(login_url='/signin/')
def student_dashboard(request):
    return render(request, 'authentication/student_dashboard.html')