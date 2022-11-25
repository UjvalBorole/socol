from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy  #this is used to convert the error according to their user country

# class CustomUserManager(BaseUserManager):
#     def create_user(self,email,password,username,**extra_field):  #extra_field have this data is comming from the BaseUSerManager is not written in the create_user function
#         if not email:
#             raise ValueError(gettext_lazy('The Email must be set'))
#         email = self.normalize_email(email)   #normalize_email means this is used convert the first Upper letter into the normal lower case its maintain the convention
#         user = self.model(email=email ,username=username,**extra_field) #it means User(email=email,**extra_field) 
#         user.set_password(password) #this is used to password convert to Hsl code 
#         user.save()
#         return user
    
#     def create_superuser(self,email,password,username,**extra_field):    #extra_field includes the is_admin, is_staff,is_superuser
#         extra_field.setdefault('is_active',True)
#         extra_field.setdefault('is_staff',True)
#         extra_field.setdefault('is_superuser',True)

#         if extra_field.get('is_staff') is not True:
#             raise ValueError(gettext_lazy('Superuser must have is_staff=True'))
#         if extra_field.get('is_superuser') is not True:
#             raise ValueError(gettext_lazy('Superuser must have is_superuser=True'))
#         return self.create_user(email, password,  username,  **extra_field)
            

class CustomUserManager(BaseUserManager) :

    def create_user(self, email, password, username, **extra_fields):
        if not email:
            raise ValueError(gettext_lazy('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, username, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(gettext_lazy('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(gettext_lazy('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, username, **extra_fields)