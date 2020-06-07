from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect 
from dashboard.models import Sales,StockItem 
import logging  
from django.views import View
# Create your views here.
def indexpage(request):  
    sales = Sales.objects.all().order_by('-pub_date')[:12] 
    return render(request, 'index.html', {'html': "page_title - home", 'sales' : sales  }) 
 
def salespage(request,salesid):  
 	# logging.warning(request) 
    ses = Sales.objects.get(id=salesid)  
    return render(request, 'salespage.html', {'html': salesid, 'sales':ses })  

def listsalespage(request):  
    sales = Sales.objects.all().order_by('pub_date')
    return render(request, 'listsales.html', {'html': "page_title - home", 'sales' : sales  })

def stockspage(request):  
    stocks =StockItem.objects.all().order_by('-pub_date')[:12] 
    return render(request, 'stocks.html', {'html': "page_title - home", 'stocks' : stocks  })      