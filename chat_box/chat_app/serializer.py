
from api.models import ChatMessages, Profile
from rest_framework import serializers




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id' , 'user' , 'full_name' , 'image']



class ChatMessagesSerializer(serializers.ModelSerializer):
    receiver_profile = ProfileSerializer(source='recipient.profile' , read_only = True)
    sender_profile = ProfileSerializer(source='sender.profile' , read_only = True)

    class Meta:
        model = ChatMessages
        fields = ['id' , 'user' , 'sender' , 'sender_profile' , 'recipient' , 'receiver_profile' , 'body' , 'is_read' , 'date']