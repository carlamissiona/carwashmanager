from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

from django.views import View
# Create your views here.
def indexpage(request):
    template = loader.get_template('index.html')
    context = {  'page_title' : 'Home' }
    # contain sales 
    # contain Staff
    return render(request, 'index.html', {'html': "page_title - home",}) 

def indexpage(request):
    template = loader.get_template('index.html')
    context = {  'page_title' : 'Home' }
    return render(request, 'index.html', {'html': "page_title - home",}) 
    # return HttpResponse(template.render(context, request))
