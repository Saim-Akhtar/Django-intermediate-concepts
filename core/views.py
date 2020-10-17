from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from .helpers import send_email

# Create your views here.
def index_view(request):
    return render(request,'core/index.html',context={})

def regsiter_view(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            auth_user = authenticate(username=username,password=password)
            login(request, auth_user)
            messages.success(request, "User registered successfully")
            return redirect('core:index')


    context = {
        'form':form
    }
    return render(request,'core/register.html',context)

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            auth_user = authenticate(username=username,password=password)
            login(request, auth_user)
            messages.info(request,"User Logged In")
            if next:
                return redirect(next)
            return redirect('/auth')


    context = {
        'form':form
    }
    return render(request,'core/login.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')

def auth_view(request):
    if request.user.is_authenticated:
        return render(request,'core/auth_page.html',context={})
    else:
        return redirect('core:login')

@login_required
def premium_view(request):
    return render(request,'core/premium.html')

class PremiumView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        return render(self.request,"core/premium.html")

def send_mail_tester(request):
    subject = "This is subject"
    message = "This is message"
    email = "sami90alam@gmail.com"
    send_email(subject,message,email)
    return redirect('/')