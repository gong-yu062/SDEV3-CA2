from django.urls import path
from shop import views
from .views import signupView, signinView, signoutView

urlpatterns = [
    path('signup/', signupView, name='signup'),
    path('login/', signinView, name='signin'),
    path('logout/', signoutView, name='signout'),
]