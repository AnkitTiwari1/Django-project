from django.shortcuts import render,redirect
from .models import information
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url="/account/login/")
def createemp(request):	
	return render(request,"Information/createemp.html")


def createemp2(request):
	if request.method=="POST":
		# a=information()
		ename=request.POST['name1']
		emob=request.POST['mob']         
		email=request.POST['email']
		eaadhar=request.POST['aadhar']
		esalary=request.POST['salary']
		# a.save()
		
		messages.success(request,f"{a.ename} is successfully created...!")
		return redirect('Information:emplist')
	return render(request,"Information/createemp.html")
		

	

def emplist(request):
	a=information.objects.all()
	return render(request,"Information/emplist.html",{'data':a})

def update(request,pk):
	print(pk)
	a=information.objects.get(id=pk)
	return render(request,"Information/updateemp.html", {'data':a})

def update2(request,pk):
	print(pk)
	if request.method=="POST":
		a=information.objects.get(id=pk)
		a.ename=request.POST['name1']
		a.emob=request.POST['mob']         
		a.email=request.POST['email']
		a.eaadhar=request.POST['aadhar']
		a.esalary=request.POST['salary']
		a.save()
		messages.success(request,f"{a.ename} is successfully Updated...!")
	return redirect("Information:emplist")


def confdel(request,pk):
	print(pk)
	a=information.objects.get(id=pk)
	return render(request,"Information/deleteemp.html", {'data':a})

def delete(request,pk):
	print(pk)
	a=information.objects.get(id=pk)
	a.delete()
	messages.success(request,f"{a.ename} is successfully Deleted...!")
	return redirect("Information:emplist")




	




