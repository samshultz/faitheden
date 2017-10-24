from django.contrib import admin

from .models import Post
# from .models import marq
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'published', 'updated']
	list_filter = ['title', 'published', 'updated' ]
	# class Meta:
	# 	model = Post

admin.site.register(Post, PostAdmin)
# admin.site.register(marq)