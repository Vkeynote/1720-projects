from django.contrib import admin
from app.models import Speaker, Track, Session

class speakerAdmin(admin.ModelAdmin):
	list_display = ["name", "bio"]

admin.site.register(Speaker, speakerAdmin)

class trackAdmin(admin.ModelAdmin):
	list_display = ["title", "description"]
	list_display_links = ["title", 'description']

admin.site.register(Track, trackAdmin)

class sessionAdmin(admin.ModelAdmin):
	list_display = ["title", "speaker"]
	search_fields = ["title", "abstract"]

admin.site.register(Session, sessionAdmin)