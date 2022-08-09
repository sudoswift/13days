from django.contrib import admin
from .models import Conversation,Message

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """Conversation Admin"""
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Message Admin"""
    pass
