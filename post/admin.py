from django.contrib import admin
from .models import Post, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 3


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "is_published"]
    list_filter = ["is_published"]
    prepopulated_fields = {
        "slug": ("title", )
    }
    inlines = [ImageInline]

admin.site.register(Post, PostAdmin)
