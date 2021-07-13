
from django.urls import path,include
from . import views
urlpatterns = [
   path("",views.home,name='home'),
   path("imdb",views.imdb,name="imdb"),
   path("hate",views.hate,name="hate")
]
