from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse -> if no templates used, use this in addition





def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request,'blog/home.html',context) #adding third arg makes post dictionary accesible  in template


	#you can actually code the entire path's page here 

def about(request):
	return render(request,'blog/about.html', {'title': 'About'})

def test(request):
	return render(request,'blog/test.html', {'title': 'Test'})

#return what we want the user to see when they're sent to this route


# Create your views here.
