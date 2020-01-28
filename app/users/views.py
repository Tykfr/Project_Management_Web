from django.shortcuts import get_object_or_404, render, reverse, HttpResponseRedirect, redirect
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth import login, authenticate, logout
from django.views.generic.detail import DetailView
# Create your views here.

from .forms import UpdateProfileForm,CustomUserCreationForm, CustomUserChangeForm
from .models import Profile, CustomUser

class RegisterView(FormView):

    """
    Gives the user the registration form
    """
    def get(self,request):
        user_form = CustomUserCreationForm()
        content = {
        'user_form':user_form,
        }
        return render(request,'registration/register.html',content)
    """
    Takes the user information and varifies it
    """
    def post(self,request):
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            user.save()
            return redirect(reverse("posts"))
        content = {"user_form":user_form}
        return render(request,'registration/register.html',content)

class LogoutView(FormView):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/')

class ProfileUpdateView(FormView):

    def get(self,request,pk):
        profile = get_object_or_404(Profile,pk=pk)
        user = profile.user
        user_form = CustomUserChangeForm(instance=user)
        profile_form = UpdateProfileForm(instance=profile)
        content = {
        "user_form":user_form,
        "profile_form":profile_form,
        }
        return render(request,'users/profile_update_form.html',content)

    def post(self,request,pk):
        profile = get_object_or_404(Profile,pk=pk)
        user = profile.user
        user_form = CustomUserChangeForm(request.POST,instance=user)
        profile_form = UpdateProfileForm(request.POST,request.FILES,instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('profile'))
        content = {
        "user_form":user_form,
        "profile_form":profile_form,
        }
        return render(request,'users/profile_update_form.html',content)

class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'

    """ Get the user profile for person viewing
        website now without pk or slug    """
    def get_object(self):
        return get_object_or_404(CustomUser,pk=self.request.user.id)
