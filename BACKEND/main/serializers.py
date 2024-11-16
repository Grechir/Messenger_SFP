from .models import Chat, Message, Profile
from django.contrib.auth.models import User
from rest_framework import serializers


class ChatSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    # отображает User через его первичный ключ (ID), и с помощью queryset берем любого пользователя

    class Meta:
        model = Chat
        fields = ('id', 'name', 'description', 'participants')


class MessageSerializer(serializers.ModelSerializer):
    chat = serializers.PrimaryKeyRelatedField(queryset=Chat.objects.all())
    sender = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ('id', 'chat', 'content', 'timestamp')


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = ('id', 'user', 'first_name', 'last_name', 'email')
