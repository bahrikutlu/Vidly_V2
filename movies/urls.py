from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),  # empty string # represents root of the app
    path('<int:movie_id>', views.detail, name='detail')
]
