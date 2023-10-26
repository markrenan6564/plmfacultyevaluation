from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from account.forms import AccountLoginForm

from account.models import *
from evaluation.models import *

# Create your views here.
def homepage(request):
	if request.user.is_authenticated:
		return render(request, "interface/dashboard.html")
	else:
		form = AccountLoginForm(request.POST or None)
		if request.method == 'POST':
			if form.is_valid():
				user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
				if user is not None:
					login(request, user)
					return render(request = request, template_name="interface/dashboard.html")
				else:
					messages.success(request, 'Invalid email or password.')
					return render(request, "interface/home.html", {"form": form})
			else:
				messages.success(request, 'Invalid username or password.')
				return render(request, "interface/home.html", {"form": form})
		else:
			return render(request, "interface/home.html", {"form": form})
 

def signup(request):
	return render(request, template_name="interface/signup.html")

def dashboard(request):
	user = get_user_model().objects.get(email=request.user.email)
	return render(request, "interface/dashboard.html", {'user': user})

def logout_view(request):
	logout(request)
	messages.success(request, 'You have been logged out.')
	return redirect('interface:homepage')

def profile(request):
	return render(request, template_name="interface/profile.html")

def evaluate(request):
	academic = Evaluation.objects.filter(account=request.user)
	return render(request, "interface/evaluate.html", {'academic': academic})

def manual_add(request):
	return render(request, template_name="interface/manual_add.html")

def duga(request):
	return render(request, template_name="interface/duga.html")

