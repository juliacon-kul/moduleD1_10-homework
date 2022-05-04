from django.urls import path
from app.models import Auto
from app import views
from app.views import SearchResultsView


app_name = 'app'
urlpatterns = [
    path('', views.autos_list),
    path('index/', views.index),
    path('index/search/',SearchResultsView.as_view(), name='search_results')
]