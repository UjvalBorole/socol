from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/',views.ProfileView.as_view(),name="profile_view"),
    path('<str:username>/edit/',views.ProfileEdit.as_view(),name="profile_edit_view"),
    path('search/',views.SearchView.as_view(),name= 'allprofile'),
   
]
