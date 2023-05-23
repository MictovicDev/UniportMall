from django.contrib import admin
from .models import *

# Register your models here.
class PostImageInLine(admin.TabularInline):
    model = PostImage


class PostCommentInline(admin.TabularInline):
    model = Comment

class PostProductInLine(admin.TabularInline):
    model = Product

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInLine, PostCommentInline,PostProductInLine]



admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Message)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OrderedItem)
admin.site.register(Comment)