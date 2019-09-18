from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout

def loginemp(request):
	print(request.method)
	if request.method=="POST":
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			return redirect("home")
	else:
		form=AuthenticationForm()
	return render(request,"Account/login.html",{'form':form})

def signup(request):
	if request.method=="POST":
		form=UserCreationForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form=UserCreationForm()
	return render(request,"Account/signup.html",{'form':form})


def logoutview(request):
	logout(request)
	return redirect("home")