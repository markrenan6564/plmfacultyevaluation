from django.shortcuts import render

# Create your views here.
def homepage(request):
	return render(request = request, template_name="interface/home.html")

def signup(request):
	return render(request, template_name="interface/signup.html")