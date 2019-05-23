from django.urls import path
from django.conf.urls.static import static
from django.urls import path
from mainapps import views

urlpatterns = [
    path('index/',views.index,name='index')
]