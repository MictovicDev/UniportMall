from django.contrib import admin
from .models import *

# Register your models here.
class PostImageInLine(admin.TabularInline):
    model = PostImage


class PostCommentInLine(admin.TabularInline):
    model = Comment

class PostProductInLine(admin.TabularInline):
    model = Product

class ChatMessageInLine(admin.TabularInline):
    model = Message

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInLine, PostCommentInLine,PostProductInLine]

class ChatAdmin(admin.ModelAdmin):
    inlines = [ChatMessageInLine,]



admin.site.register(Post, PostAdmin)
admin.site.register(Chat)
admin.site.register(Like)
admin.site.register(Message)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OrderedItem)
admin.site.register(Comment)