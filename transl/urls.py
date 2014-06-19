from django.conf.urls import patterns, url
from transl import views
from transl.models import Choice


urlpatterns = patterns(' ',
    url(r'^$', views.index, name='index'),
        

                       
   

)
