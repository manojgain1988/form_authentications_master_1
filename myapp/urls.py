from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contactPage, name='contact'),
    path('register/',views.registerPage, name='register'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutPage, name='logout'),
]
