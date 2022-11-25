from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.contrib.auth.models import User
from crum import get_current_user


Gender_choices = [('M','Male'),('F','Female'),('None','Prefer not to say')]

class Profile(models.Model):   #we create the model but inherited AbstractUser ,AbstractUser is the User model but not completed means the data include but not save and create the main User Module

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    full_name = models.CharField(max_length=100, help_text='Help people discover your account by using the name you\'re known by: either your full name, nickname, or business name.')
    # email = models.EmailField(unique=True)

    #Optional Field
    bio = models.TextField(null = True,blank=True, help_text='Provide your personal information, even if the account is used for a business, a pet or something else. This won\'t be a part of your public profile.')
    website = models.URLField(null = True,blank=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    gender = models.CharField(max_length=10,choices=Gender_choices,null=True,blank=True)
    is_private_account = models.BooleanField(null=True,blank=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS= ['full_name','username',] 

    # first_name = None
    # last_name = None

    # objects = CustomUserManager() # we are using our Customizing model

    def __str__(self):
        return self.user.email
    
    def save(self,*args,**kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:     #pk will get at the time the model was built means the data save then get the primary key
            self.user = user
        super(Profile,self).save(*args,**kwargs)

    
    def username(self):
        return self.user.username
    
    def email(self):
        return self.user.email
 
    @property
    def follower_count(self):
        count = self.follow_followed.count()    #it counts the current instance user has how much followings 
        return count
    
    @property
    def following_count(self):
        count= self.follow_follower.count()
        return count
    
    