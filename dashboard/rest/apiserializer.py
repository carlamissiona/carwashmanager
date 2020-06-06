from rest_framework import serializers

from dashboard.models import Users, StockItem, Sales

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password','email', 'firstname','lastname', 'country',   )

class StockItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StockItem
        fields = ('name', 'description' ,'qty')

class SalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sales
        fields = ('car_qty', 'sale_amount' ,'service','staff')
