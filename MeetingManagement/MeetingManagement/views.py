
from django.shortcuts import render, redirect, HttpResponse
from meeting.EmailBackEnd import EmailBackEnd

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.http import HttpResponseForbidden

from django.contrib import messages


def LOGIN(request):
    return render(request, 'login.html')



@csrf_protect
def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),)
        print(user)
        if user is not None:
            user_type = user.user_type
            if user_type == '1':
                login(request, user)
                return redirect('admin_home')
            elif user_type == "2":
                login(request, user)
                return redirect('cao_home')
            elif user_type == "3":
                login(request, user)
                return redirect('branch_home')
            elif user_type == "4":
                login(request, user)
                return redirect('chairman_home')
            else:
                messages.error(request, "Email and Password are Invalids")
                return redirect('login')
        
        messages.error(request, "Email and Password are Invalid")
        return redirect('login')

    return HttpResponseForbidden("Forbidden")




def ADMIN_HOME(request):
    return render(request,"Admin/home.html")