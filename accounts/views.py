from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic import CreateView, UpdateView, DetailView
from .models import Profile

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserEditView(UpdateView):
    model = Profile()
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.profile

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_object(self):
       return self.request.user