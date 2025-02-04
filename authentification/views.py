from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

#Create your views here.

def register_view(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('thanks')
  else:
    form = UserCreationForm()
    return render(request, 'authentification/register.html', {'form': form})
  

# class RegisterCreateView(CreateView):
#     form_class = UserCreationForm
#     template_name = 'authentification/register.html'
#     success_url = '/'


class ThankyouView(TemplateView):
    template_name = 'authentification/thanks.html'