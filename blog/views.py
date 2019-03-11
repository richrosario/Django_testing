from django.shortcuts import render
#from django.http import HttpResponse -> if no templates used, use this in addition


posts = [
	{
		'author': 'Richard',
		'title': 'My first post',
		'content': 'First post content',
		'date_posted': '3/11/19'

	},

	{
		'author': 'Chisca',
		'title': 'My second post',
		'content': 'Second post content',
		'date_posted': '3/13/19'

	}

]



def home(request):
	context = {
		'posts': posts
	}
	return render(request,'blog/home.html',context) #adding third arg makes post dictionary accesible  in template


	#you can actually code the entire path's page here 

def about(request):
	return render(request,'blog/about.html', {'title': 'About'})

def test(request):
	return render(request,'blog/test.html', {'title': 'Test'})

#return what we want the user to see when they're sent to this route


# Create your views here.
