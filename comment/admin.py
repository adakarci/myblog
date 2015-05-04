from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ["email", "owner", "body"]

admin.site.register(Comment, CommentAdmin)
