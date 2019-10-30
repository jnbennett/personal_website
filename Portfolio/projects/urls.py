from django.urls import path 
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	path('', views.Home.as_view(), name='home'),
	path('about/', views.About.as_view(), name='about'),
	path('projects/', views.Projects.as_view(), name='projects'),
	path('poetry/', views.poem_list, name='poem_list'),
	# path('<int:pk>/', views.project_detail, name='project_detail'),
]