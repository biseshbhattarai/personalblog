from django.contrib import admin
from .models import MessageForm, Subscription


admin.site.register(MessageForm)
admin.site.register(Subscription)