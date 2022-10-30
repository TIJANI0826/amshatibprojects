from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def service_detail(request):
    return render(request, 'service-details.html')
