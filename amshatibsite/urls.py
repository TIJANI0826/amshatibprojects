from django.urls import path
from . import views
app_name = "amshatibsite"
urlpatterns = [
    path('', views.home, name="index"),
    path('about', views.about, name="about"),
    path('projects', views.projects, name="projects"),
    path('services', views.services, name="services"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contact"),
    path('service-detail', views.service_detail, name="service-details")
    
]
