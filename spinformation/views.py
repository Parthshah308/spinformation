from django.shortcuts import render,HttpResponse,redirect
from spinformation.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
	return render(request, 'index.html')

def projects(request):
	return render(request, 'project.html')


def cheats(request):
	return render(request, 'cheats.html')

def git(request):
	return render(request, 'git.html')

def cdn(request):
	return render(request, 'cdn.html')

def android(request):
	return render(request, 'android.html')

def python(request):
	return render(request, 'python.html')

def java(request):
	return render(request, 'java.html')


def clang(request):
	return render(request, 'clang.html')


def cplus(request):
	return render(request, 'cplus.html')


def dsalgo(request):
	return render(request, 'dsalgo.html')


def php(request):
	return render(request, 'php.html')

def contact(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		phone=request.POST['phone']
		content=request.POST['content']
		
		if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<5:
			messages.error(request, 'Please fill the form correctly...')
		else:
			contact=Contact(name=name,email=email,phone=phone,content=content)
			messages.success(request, 'Your Information is submitted.')
			contact.save()
	return render(request, 'index.html')

def handlesignup(request):
	if request.method=='POST':	
		username=request.POST['username']
		email=request.POST['email']
		pass1=request.POST['password']
		pass2=request.POST['cpassword']

		if pass1 != pass2:
			messages.error(request, 'PASSWORD do not match.')
			return redirect('/')

		myuser=User.objects.create_user(username,email,pass1)
		myuser.save()
		messages.success(request, 'Account created successfully.')
		return redirect('/')
	else:
		return HttpResponse('page -404 not found')

def handlelogin(request):
	if request.method=='POST':
		logusername=request.POST['logemail']
		logpass=request.POST['logpass']

		user=authenticate(username=logusername,password=logpass)

		if user is not None:
			login(request, user)
			messages.success(request, 'successfully logged in.')
			return redirect('/')
		else:
			messages.error(request, 'invalid credentials,Please try again later.')
			return redirect('/')

	else:
		return HttpResponse('page -404 not found')


def handlelogout(request):
	# if request.method=="post":
		logout(request)
		messages.success(request, 'successfully logout.')
		return redirect('/')

