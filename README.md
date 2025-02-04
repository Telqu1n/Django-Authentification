# Django-Authentification
## Part 1 - This is to create a Sign-Up form which will save the user to the django user

- First import:
	- `from django.contrib.auth.forms import UserCreationForm`
- Then you need to add the form into your view with:
	- `form = UserCreationForm()`
	- Then where you render your template you need to pass in `{ "form" : form}`
```python
def register_view(request):
	form = UserCreationForm()
	return render(request, { "form": form } )
```

- Now we need to add some extra code to the template to make the form work
	- Now we need to add a form tag
	- Add the action of the form to submit to the same form page  
		- `<form action = authentification/register/`

![image](https://github.com/user-attachments/assets/e5dab845-8175-40e0-98eb-a580b6a02ba4)
	- Next in the form tag add `method = POST`
	- Now inside the form tags is where we will use the form provided by django.
	- `{{ form }}`
	- Then add a button
		- If only one button is used in a form it will automatically default to a submit button 
	- Then make sure to add the csrf_token
		- `{% csrf_token %}`
```python html
{% block content %}
	<form action:"/authentification/register/" "method: "post" >
	{% csrf_token %}
		{ { form } }
		<button> Submit </button>
	</form>
{% endblock %}
```

# MAKE SURE TO MIGRATE 

- Now we need to save the submission
- so go the app level views.py
- Now me need to import the redirect function
- `from django.shortcuts import render, reqirect`
- Now we are using a if statement 
	- `if request.method == "POST"`:
	- Anything under this statement will be done if the form is submitted 
	- Then add `form = UserCreationForm(request.POST)`
		- Passing in the information we have saved
	- Inside the if statement we have another if statement 
	- `if form.is_valid():`
		- `form.save()`
	- If the form is saved we will then redirect to 
``` python
def register_view(request):
	if request.method == "POST":
	form = UserCreationForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect("")
else:
	form = UserCreationForm
	return render(request,"users/register.html" { "form": form})
```
### This can be made more simple by using the `CreateView`
- To do this first go to views.py import:
  	- `from django.views.generic.edit import CreateView `
  	- Then create your view
  	- linking form_class to UserCreationForm
  	- ```python
  	  class RegisterCreateView(CreateView):
   		form_class = UserCreationForm
    		template_name = 'authentification/register.html'
    		success_url = 'thanks'
  	  ```
- Then to link this form go to urls.py in your app folder
- The add this url
 	- `path('', views.RegisterCreateView.as_view(), name='register'),`
  - Make sure the success_url is linking to the name of another page you want to go to if the form is successfull
  - for me:
   	- `path('thanks/', views.ThankyouView.as_view(), name='thanks'),` 



