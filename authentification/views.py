from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm, CustomLogInView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
#Create your views here.

# def register_view(request):
#   if request.method == "POST":
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       login(request, form.save())
#       return redirect('thankyou')
#     return render(request, 'authentification/register.html', {'form': form})

#   else:
#     form = UserCreationForm()
#     return render(request, 'authentification/register.html', {'form': form})
   
    
# def login_view(request): 
#     if request.method == "POST": 
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid(): 
#             login(request, form.get_user())
#             return redirect("thankyou")
#         return render(request, 'authentification/register.html', {'form': form})

#     else: 
#         form = AuthenticationForm()
#     return render(request, "authentification/login-page.html", { "form": form })  
  
   
# def logout_view(request):
#     if request.method =="POST":
#         logout(request)
#         return redirect('thankyou')


class RegisterCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'authentification/register.html'
    success_url = 'thankyou'
    
    def form_valid(self, form):
            response = super().form_valid(form)
            user = self.object  # Get the newly created user
            login(self.request, user)  # Log the user in
            return response

     
class LoginView(LoginView):
    template_name = "authentification/login-page.html"
    authentication_form = AuthenticationForm  # Uses Django's default login form
    redirect_authenticated_user = True  # Prevent logged-in users from seeing the login page
    next_page = reverse_lazy("thankyou")  # Redirect after successful login     
            


class LogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect after logout




class ThankyouView(TemplateView):
    template_name = 'authentification/thankyou.html'

class Thankyou2View(TemplateView):
    template_name = 'authentification/thankyou.html'
   
   
