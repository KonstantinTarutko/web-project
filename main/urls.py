from django.urls import path
from . import views
from .views import sending_form, sending_second_form

app_name = 'main'

urlpatterns = [
    #    path('', views.index, name='home'),
    path('', sending_form, name='home'),
    path('about', views.about, name='about'),
    path('contacts', sending_second_form, name='contacts'),
]
