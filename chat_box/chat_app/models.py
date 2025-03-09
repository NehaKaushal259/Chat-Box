from django.db import models

from django.contrib.auth.models import User 


# Create your models here.


class ChatMessages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    body = models.TextField(null=True)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def sender_message(from_user, to_user, body):
        sender_message = ChatMessages(
            user = from_user,           # Because you started to conversation
            sender = from_user,         # Because you sent the first message 
            recipient = to_user,       # Because you are getting a message
            body = body,
            is_read = True,              # The sender immediately sees it as read
        )

        sender_message.save()

        recipient_message = ChatMessages(
            user = to_user,             # Message belongs to the recipient
            sender = from_user,
            recipient = to_user,
            body = body,
            is_read = False ,        # Recipient hasn't read it yet
        )

        recipient_message.save()

        return sender_message


    def get_message(user):
        users = []  # List to store chat details

        all_messages = ChatMessages.objects.filter(user=user)                       # Get all messages where the user is involved

        unique_recipients = set(all_messages.values_list('recipient', flat=True))   # Get unique recipients that the user has chatted with

        for recipient_id in unique_recipients:
            recipient = User.objects.get(pk=recipient_id)                           # Get the user object for the recipient

            last_message = all_messages.filter(recipient=recipient).order_by('-date').first()  # Get the latest message with this recipient

            unread_count = all_messages.filter(recipient=recipient, is_read=False).count()      # Count unread messages from this recipient

            users.append({                                            # Add details to the list
                'user': recipient,                                    # The chat partner
                'last': last_message.date if last_message else None,  # Last message timestamp
                'unread': unread_count                                # Unread messages count
            })

        return users
