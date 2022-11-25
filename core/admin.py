from django.contrib import admin
from .models import Post,Comment,Like,Follow

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['text','image','user' , 'update_on','created_on']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text','post','user' , 'update_on','created_on']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['post','is_like','user' , 'update_on','created_on']

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['followed','user' , 'updated_on','followed_on']
