from django.contrib import admin

# Register your models here.
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'status','created_on')
    list_filter = ('status',)
    search_fields = ['id','title', 'content']
    prepopulated_fields = {'slug': ('title',)}
class CommentAdmin(admin.ModelAdmin):
    list_display =('id','author','body','created_on','post')
    search_fields = ['id','author','post' ]
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)