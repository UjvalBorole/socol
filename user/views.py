from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .forms import UserEditForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .models import Profile as ps

from core.models import Follow

# User = get_user_model()

# Create your views here.
class ProfileView(View):
    template_name = 'core/pro.html'
    def get(self,request ,*args,**kwargs):
        username = kwargs.get('username')
        follow=' '
        id = User.objects.get(username = username)
        # follow = Follow.objects.all()
        print(follow)

        try:
            data = ps.objects.get(user = id.id)
        except Exception as e: 
            # follow=' '
            data = id  

        # try:
        # print(Profile)
        # except Exception as e:
        #     return HttpResponse('<h1>This Page does not exist.</h1>')

        if username == request.user.username:
            context = {'user':data,'follow':follow}
            return render(request,'core/pro1.html',context)
        
        else:
            context = {'user':data,'follow':follow}
            return render(request,'core/pro.html',context)
        

class ProfileEdit(View):
    template_name = 'core/profile_edit.html'
    # form_class = UserEditForm()

    def get(self,request,*args,**kwargs):
        username = kwargs.get('username')
        id = User.objects.get(username=username)
        pic = ps.objects.get(user = id)
        profile = ps.objects.get(user=request.user)
        if username != request.user.username:
            return HttpResponse("<h1>This Page is doesn't exist</h1>")
        form = UserEditForm(instance=profile)
        context = {'form':form,'pic':pic}
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        profile = ps.objects.get(user=request.user)
        form = UserEditForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view',request.user.username)
        
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += 'is-invalid'
            context = {'form':form}
            return render(request,self.template_name,context)
        
@method_decorator(csrf_exempt, name='dispatch')
class Allprofile(View):
    template_name = 'core/all_profiles.html'
  
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query')
        username = kwargs.get('username')
        print('username',username)
        print(query)
        if query:
            all_profiles = User.objects.filter(
                    Q(username__contains=query) | Q(full_name__contains=query)
                ).exclude(
                    username=request.user.username
                )
        else:
            all_profiles = User.objects.none()

        context = {'all_profiles': all_profiles}
        return render(request, self.template_name, context)
    

class SearchView(ListView):
    # model = Product
    template_name = 'core/all_profiles.html'
    context_object_name = 'all_profiles'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('query')
        # print(query)
        if query:
            postresult = User.objects.filter(username__contains=query)
            result = postresult
        else:
            result = None
        return result
