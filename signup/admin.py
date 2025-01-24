from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'signup_date')
    search_fields = ('email',)
