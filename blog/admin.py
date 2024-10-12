from django.contrib import admin
from .models import PostModel, CommentPost

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)

admin.site.register(PostModel, PostModelAdmin)
admin.site.register(CommentPost)


