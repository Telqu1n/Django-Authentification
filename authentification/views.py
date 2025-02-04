from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register_view(request):
    form = UserCreationForm()
    return render(request, 'authentification/register.html', {'form': form})