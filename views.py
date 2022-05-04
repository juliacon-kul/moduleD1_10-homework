from django.shortcuts import render
from app.models import Auto
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.db.models import Q
from django.urls import reverse_lazy


# Create your views here.
def autos_list(request):
    autos = Auto.objects.all()
    return HttpResponse(autos)

def index(request):
    template = loader.get_template('index.html')
    autos_count = Auto.objects.all().count()
    auto_data = {"title": "мою коллекцию", "autos_count": autos_count}
    autos = Auto.objects.all()
    auto_data = {
        "title": "мою коллекцию",
        "autos_count": autos_count,
        "autos": autos,
    }
    return HttpResponse(template.render(auto_data))


class SearchResultsView(ListView):
    model = Auto
    template_name = 'index.html'
    queryset = Auto.objects.filter(manufacturer__icontains='F')

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Auto.objects.filter(
            Q(model__icontains=query) | Q(manufacturer__icontains=query)
        )
        return object_list
