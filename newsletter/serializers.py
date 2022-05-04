from rest_framework import serializers
from .models import Tag, Newsletter
from django.contrib.auth.models import User


class NewsletterSerializer(serializers.ModelSerializer):
    # tags = TagSerializer(Tag, many=True)
    class Meta:
        model = Newsletter
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    newsletters = NewsletterSerializer(Newsletter, read_only=True, many=True)

    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# class GuestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Newsletter_Guest
#         fields = '__all__'
