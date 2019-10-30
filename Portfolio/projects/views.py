from django.shortcuts import render
from projects.models import Poem
from django.views.generic import TemplateView


class Home(TemplateView):
	template_name = 'projects/home.html'

class About(TemplateView):
	template_name = 'projects/about.html'

class Projects(TemplateView):
	template_name = 'projects/project_index.html'

class Poetry(TemplateView):
		template_name = 'projects/project_index.html'


def poem_list(request):
	poems = Poem.objects.all()
	return render(request, 'projects/project_index.html', {'poems': poems})