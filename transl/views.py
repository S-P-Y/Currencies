from django.http import HttpResponse
from django.template import RequestContext
from transl.models import Choice
from django.shortcuts import render_to_response
from django.template import Context, loader




def index(request):

    lists = Choice.objects.all()
    

    t = loader.get_template('index.html')
    c = Context({
        'lists': lists,

       })

        
    return HttpResponse(t.render(c))


