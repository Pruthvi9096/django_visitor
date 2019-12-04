from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.forms import SignUpForm,AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib import auth

def home(request):
	return render(request,'home.html')

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():	
        user = form.save()
        user.refresh_from_db()
        # user.profile.first_name = form.cleaned_data.get('first_name')
        # user.profile.last_name = form.cleaned_data.get('last_name')
        # user.profile.email = form.cleaned_data.get('email')
        # user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				
				return redirect('/visitor_app/visit')
			else:
				return HttpResponse("Your Account is Disabled")
		else:
			print ("Invalid login details: {0},{1}".format(username,password))
			return HttpResponse("Invalid login details supplied")
	else:
		form = AuthenticationForm()
	return render(request,'login.html',{'form':form})

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')