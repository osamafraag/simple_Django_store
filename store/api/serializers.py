from rest_framework import serializers
from store.models import Product
from rest_framework.validators import UniqueValidator

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100,validators=[UniqueValidator(queryset=Product.objects.all())])
    price = serializers.IntegerField()
    image = serializers.ImageField(allow_null=True, allow_empty_file=True)
    instock = serializers.BooleanField(default=True)
    description = serializers.CharField(max_length=300)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        return Product.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.price = validated_data.get('price')
        instance.instock = validated_data.get('instock')
        instance.description = validated_data.get('description')
        instance.image = validated_data.get('image')
        instance.save()
        return  instance