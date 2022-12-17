from rest_framework import serializers
from .models import bookPurchased

class bookPurchasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookPurchased
        fields = '__all__'
