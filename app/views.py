from django.shortcuts import render
from .models import *

# Create your views here.
def page(request):
    return render(request,"app/registration.html")

def LoginPage(request):
    return render(request,"app/login.html")

def RegisterUser(request):
    try:
        if request.POST['role'] == 'doctor':
            role = request.POST['role']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            password = request.POST['password']
            confirmpassword = request.POST['confirmpassword']
            gender = request.POST['gender']
            email = request.POST['email']
            speciality = request.POST['speciality']
            dateofbirth = request.POST['birthdate']
            city = request.POST['city']
            mobile = str(request.POST['phone'])

            user = User.objects.filter(email=email)
            if user:
                message = 'This email already exists'
                return render(request, 'app/registration.html', {'message': message})
            else:
                if password == confirmpassword:
                    newuser = User.objects.create(
                        email=email, password=password, role=role)
                    newdoctor = Doctor.objects.create(user_id=newuser, firstname=firstname, lastname=lastname,
                                                      gender=gender, speciality=speciality, city=city, mobile=mobile, birthdate=dateofbirth)            
                    return render(request, 'app/LOGIN.html')
                else:
                    message = "Password and confirm password doesn't match"
                    return render(request, 'app/registration.html', {'message': message})

        else:
            role = request.POST['role']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            password = request.POST['password']
            confirmpassword = request.POST['confirm']
            gender = request.POST['gender']
            email = request.POST['email']
            dateofbirth = request.POST['birthdate']
            city = request.POST['city']
            mobile = str(request.POST['phone']) 
            user = User.objects.filter(email=email)
            if user:
                message = 'This email already exists'
                return render(request, 'app/registration.html', {'message': message})
            else:
                if password == confirmpassword:
                    newuser = User.objects.create(
                        email=email, password=password, role=role)
                    newpatient = Patient.objects.create(
                        user_id=newuser, firstname=firstname, lastname=lastname, gender=gender, city=city, mobile=mobile, birthdate=dateofbirth)
                    return render(request, 'app/login.html')
                else:
                    message = "Password and confirm password doesn't match"
                    return render(request, 'app/registration.html', {'message': message})
    except User.DoesNotExist:
        message = 'This email already exists'
        return render(request, 'app/registration.html', {'message': message})


def LoginUser(request):
    if request.POST['role'] == 'doctor':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)
        print(user)
        if user[0]:
            if user[0].password == password and user[0].role == 'doctor':
                return render(request,"app/home.html")
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "app/login.html", {'message': message})
        else:
            message = "user doesn't exist"
            return render(request, "app/login.html", {'message': message})

    if request.POST['role'] == 'patient':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)
        print(user)
        if user[0]:
            if user[0].password == password and user[0].role == 'patient':
                return render(request,"app/home.html")
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "app/login.html", {'message': message})
        else:
            message = "user doesn't exist"
            return render(request, "app/login.html", {'message': message})