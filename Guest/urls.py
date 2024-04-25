from django.contrib import admin
from django.urls import path

from Guest import views

app_name="Guest"

urlpatterns = [
    path('admin/', admin.site.urls),

    #New User

    path('NewUser/',views.userRegistration,name="userRegistration"),
    path('NewSeller/',views.sellerRegistration,name="sellerRegistration"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    path('',views.HomePage,name="HomePage"),

    path('Login/',views.Login,name="Login"),

    
]
