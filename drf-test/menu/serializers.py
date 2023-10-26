from rest_framework import serializers

from .models import Item, User, Source_location


class Source_locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source_location
        fields = '__all__'

class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    source = Source_locationSerializer()

    class Meta:
        model = Item
        # fields = ('name', 'price', 'description')
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    favorite_item = ItemSerializer()

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'favorite_item': {'write_only': True},
        }
