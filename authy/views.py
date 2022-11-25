from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistration
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate, 
    login, logout, 
    # get_user_model,
    
    )
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
    )
# User = get_user_model()

class signup(View):
    template_name = 'authentication/signup.html'
    form_class = UserRegistration

    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
            # return redirect('home_feed_view')
       
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
       
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {'form': form}

        return render(request, self.template_name, context)
    

class loginview(View):
    template_name = 'authentication/signin.html'

    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
            # return redirect('home_feed_view')
        return render(request, self.template_name)

    def post(self, request):
        email_username = request.POST.get('email_username')
        password = request.POST.get('password')
        
        try:
            user_obj = User.objects.get(email=email_username)  #to grab the data through email and username
            if user_obj is not None:
                userName=user_obj.username
            else:
                userName= user_obj.email
        except Exception as e:
            userName = email_username

        user = authenticate(request, username=userName , password=password)
        
        if user is None:
            messages.error(request, 'Invalid Login.', extra_tags="error")
            return render(request, self.template_name) 

        login(request, user)
        messages.success(request, 'Thanks for Login, Welcome to SOCOL.', extra_tags='success')
        return redirect('index')

class PRView(PasswordResetView):
    email_template_name = 'authentication/password_reset_email.html'
    template_name = 'authentication/password_reset.html'

class PRDone(PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html'

class PRConfirm(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'

class PRComplete(PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'


class PWDChangeView(PasswordChangeView):
    template_name = 'authentication/password_change.html'
    success_url = 'password_change_done_view'

class PWDChangeDoneView(PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'


