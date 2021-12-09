from django.urls import path
from .views import SignUpView, UserEditView, ProfilePageView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('user_profile/', ProfilePageView.as_view(), name='user_profile'),
]