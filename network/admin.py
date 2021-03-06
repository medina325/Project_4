from django.contrib import admin

from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "profile_pic_url")
    filter_horizontal = ("followers",)

class PostAdmin(admin.ModelAdmin):
    list_display = ("poster","number_likes", "content")
    filter_horizontal = ("likers",)

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)

