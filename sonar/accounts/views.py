# Import statements
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Signup function
def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			# Log the user in
			login(request, user)
			return redirect('articles:list')
	else:
		form = UserCreationForm()
	return render(request, 'accounts/signup.html', {'form': form})


# Login Function
def login_view(request):
	if request.method == 'POST':
		# Have to add 'data' - because not naturally first parameter of this function
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			# Log in the user
			user = form.get_user()
			login(request, user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			return redirect('articles:list')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form': form})


# Logout Function
def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('articles:list')


