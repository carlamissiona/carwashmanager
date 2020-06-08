from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect 
from dashboard.models import Sales,StockItem

# # from django.views.decorators.http import require_POST  -- use with decorator above methofd
# @require_POST
# def cart_add(request, product_id): 

import logging  
from django.views import View
# Create your views here.
def indexpage(request):
    sales = Sales.objects.all().order_by('-pub_date')[:12] 
    return render(request, 'index.html', {'html': "page_title - home", 'sales' : sales  }) 
 
def salespage(request,salesid):  
 	# logging.warning(request) 
    # ses = Sales.objects.get(id=salesid)
    ses = get_object_or_404(Sales,
                            id=salesid )
    return render(request, 'salespage.html', {'html': salesid, 'sales':ses })  

def listsalespage(request):  
    sales = Sales.objects.all().order_by('pub_date')
    return render(request, 'listsales.html', {'html': "page_title - home", 'sales' : sales  })

def stockspage(request):  
    stocks =StockItem.objects.all().order_by('-pub_date')[:12] 
    return render(request, 'stocks.html', {'html': "page_title - home", 'stocks' : stocks  })      