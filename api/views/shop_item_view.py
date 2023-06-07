from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from api.models import ShopItem

class ShopItemView(ViewSet):
  def retrieve(self, request, pk=None):
    shop_item = ShopItem.objects.get(pk=pk)
    serialized = ShopItemSerializer(shop_item, context={'request': request})
    return Response(serialized.data, status=status.HTTP_200_OK)
  
  def list(self, request):
    shop_item = ShopItem.objects.all()
    serialized = ShopItemSerializer(shop_item, many=True)
    return Response(serialized.data, status=status.HTTP_200_OK)
  
  def create(self, request):
    shop_item = ShopItem()
    
    shop_item.name = request.data["name"]
    shop_item.description = request.data["description"]
    shop_item.purchase_url = request.data["purchase_url"]
    shop_item.save()
    
    serialized = ShopItemSerializer(shop_item, many=False)
    return Response(serialized.data, status=status.HTTP_200_OK)

class ShopItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = ShopItem
    fields = ('id','name','description','purchase_url')
