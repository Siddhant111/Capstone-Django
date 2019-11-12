from django.conf.urls import url
from . import views

app_name = 'preventative'

urlpatterns = [
    url('preventative/', views.preventative, name = 'preventative'),
    url('preventative_test/', views.preventative_test, name = 'preventative_test'),
]