from django.shortcuts import render
from django.views import View
from nbconvert import HTMLExporter
from nbformat import read
from .models import Project, Menu


# Create your views here.

class Index(View):
    template = 'videos/index.html'

    def get(self, request):
        menu = Menu.objects.prefetch_related('project_set').all()

        context = {'menu': menu}

        return render(request, self.template, context)


# pour recharger les projets dans la page main
def recharge_projet_notebook(request):
    id = request.GET.get('project_id')
    project = Project.objects.get(pk=id)
    menu = Menu.objects.prefetch_related('project_set').all()

    path = project.notebook.path
    exporter = HTMLExporter()
    notebook, _ = exporter.from_file(path)

    context = {'project': project, 'notebook': notebook, 'menu': menu}

    return render(request, 'videos/notebook.html', context)
