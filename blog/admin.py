from django.contrib import admin
from .models import Post, Comment

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "created_date")

admin.site.register(Post, EntryAdmin)
admin.site.register(Comment)