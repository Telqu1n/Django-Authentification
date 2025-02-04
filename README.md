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

# Creating a log-in form and making it so that a user will be logged in after they register and account 
 Create your path for your new log in page 
- Now we go to views.py 
- and add our new login function 
	- `def login_view(request)`

- In the function we will also add 
	- `if request.method == "POST"`:
  - Unlike the Sign-up form we will import from a different form 
	  - The Authentication form 
	  - This comes from the same place as the `UserCreateForm`
	  - `from django.contrib.auth.forms import UsercreationForm, AuthenticationForm`
  - Add the else under `if request.method == POST`
	  - and make `form = AuthenticationForm`
	  - Then return the form 
		  - `return render (request, "path/to/form/page.html, {"form": form})"`
- Now directly under `if request.method == "POST"`
- add ` form = AuthenticationForm`

- Now create your login form

- Now in `from = AuthenticationForm()`
	- We don't pass in `request.post`
	- We have to pass in `data=request.post`
	- `form = AuthenticationForm(data=request.post)`
- Now we can add `if form.is_valid():`
- Unlike the Creation form we do now use `form.save()`
- So leave that line blank and under it ass a return redirect 
```python
def login_view(request): 
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
			#LOGIN HERE
            return redirect("posts:list")
    else: 
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form": form })
```
- Now we need to import one more thing:
- `from django.contrib.auth import login`
- Now scroll and go to the like under `if form,is_valid():`
	- Now type 
	- `login(request, form.get_user())`
	- This calls the user to then check so see if it matches, which what is stored 
```python
def login_view(request): 
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            login(request, form.get_user())
            return redirect("")
    else: 
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form": form })
```
- Now to make a user get logged in directly after they sign up you can do this:
	- Add the `login()` to `form.save()`
	- `login(request, form.save())`
```python
def register_view(request):
    if request.method == "POST": 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            login(request, form.save())
            return redirect("")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", { "form": form })
```

### I don't know if this can be done as a class view so I will keep it as a function view

