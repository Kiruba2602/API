from rest_framework import serializers
from .models import MenuItem, Category, Rating, Order, OrderItem, Cart
from rest_framework.validators import UniqueTogetherValidator 
from django.contrib.auth.models import User

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory','featured','category','category_id']
        
class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
            queryset = User.objects.all(),
            default = serializers.CurrentUserDefault()
    )
    class Meta:
        model = Rating
        fields = ['user','menuitem_id','rating']
        validators = [
            UniqueTogetherValidator(
                queryset = Rating.objects.all(),
                fields = ['user','menuitem_id','rating']
            )
        ]
        extra_kwargs = {
            'rating': {
                'max_value': 5,
                'min_value': 0,
            }
        }
        
class ManagerListSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['id','username','email']

class CartHelpSerializer(serializers.ModelSerializer):
    class Meta():
        model = MenuItem
        fields = ['id','title','price']

class CartSerializer(serializers.ModelSerializer):
    menuitem = CartHelpSerializer()
    class Meta():
        model = Cart
        fields = ['menuitem','quantity','price']
        
class CartAddSerializer(serializers.ModelSerializer):
    class Meta():
        model = Cart
        fields = ['menuitem','quantity']
        extra_kwargs = {
            'quantity': {'min_value': 1},
        }
class CartRemoveSerializer(serializers.ModelSerializer):
    class Meta():
        model = Cart
        fields = ['menuitem']

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['username']

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta():
        model = Order
        fields = ['id','user','total','status','delivery_crew','date']

class SingleHelperSerializer(serializers.ModelSerializer):
    class Meta():
        model = MenuItem
        fields = ['title','price']
        
class SingleOrderSerializer(serializers.ModelSerializer):
    menuitem = SingleHelperSerializer()
    class Meta():
        model = OrderItem
        fields = ['menuitem','quantity']

class OrderPutSerializer(serializers.ModelSerializer):
    class Meta():
        model = Order
        fields = ['delivery_crew']