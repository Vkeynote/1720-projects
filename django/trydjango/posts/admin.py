from django.contrib import admin
from .models import Post

class postAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp", "updated", "content"]
	list_display_links = ["title", "content"]
	list_filter = ["timestamp", "updated"]
	# save_on_top = True
	class Meta:
		model = Post 

admin.site.register(Post, postAdmin)

