from rest_framework import viewsets
from dashboard.models import User, Sales, StockItem
from .  import apiserializer 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = apiserializer.UserSerializer
class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all().order_by('staff')
    serializer_class = apiserializer.SalesSerializer
class StockItemViewSet(viewsets.ModelViewSet):
    queryset = StockItem.objects.all().order_by('name')
    serializer_class = apiserializer.StockItemSerializer