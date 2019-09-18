from django.shortcuts import render, redirect
from .models import post


# Create your views here.
def addpost(request):
	return render(request,"Post/addpost.html")

def addpost2(request):
	if request.method=="POST":
		p=post()
		p.title=request.POST["title"]
		p.author=request.POST["author"]
		p.post=request.POST["post"]
		p.file=request.FILES["file"]
		p.save()
		return redirect("allpost")
	return render(request,"Post/addpost.html")

def allpost(request):
	p=post.objects.all().order_by('date')
	return render(request,"Post/allposts.html",{'data':p})





