from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'published', 'updated']
	list_filter = ['title', 'published', 'updated' ]
	# class Meta:
	# 	model = Post

admin.site.register(Post, PostAdmin)
