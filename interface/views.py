from django.shortcuts import render

excluded_urls = ['home.html', 'signup.html']

# Create your views here.
def homepage(request):
	return render(request = request, template_name="interface/home.html", context={"excluded_urls": excluded_urls})

def signup(request):
	return render(request, template_name="interface/signup.html", context={"excluded_urls": excluded_urls})

def dashboard(request):
	return render(request, template_name="interface/dashboard.html", context={"excluded_urls": excluded_urls})

def profile(request):
	return render(request, template_name="interface/profile.html", context={"excluded_urls": excluded_urls})

def evaluate(request):
	return render(request, template_name="interface/evaluate.html", context={"excluded_urls": excluded_urls})
