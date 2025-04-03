from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('username', 'full_name')
    ordering = ('order', 'username')
