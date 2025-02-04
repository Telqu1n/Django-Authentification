from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

#Create your views here.

def register_view(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      login(request, form.save())
      return redirect('thankyou')
    return render(request, 'authentification/register.html', {'form': form})

  else:
    form = UserCreationForm()
    return render(request, 'authentification/register.html', {'form': form})
   
   
    
def login_view(request): 
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            login(request, form.get_user())
            return redirect("thankyou")
        return render(request, 'authentification/register.html', {'form': form})

    else: 
        form = AuthenticationForm()
    return render(request, "authentification/login-page.html", { "form": form })  
  
   
# class RegisterCreateView(CreateView):
#     form_class = UserCreationForm
#     template_name = 'authentification/register.html'
#     success_url = 'thanks'


class ThankyouView(TemplateView):
    template_name = 'authentification/thanks.html'

class Thankyou2View(TemplateView):
    template_name = 'authentification/thankyou.html'
   