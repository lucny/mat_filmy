from django.contrib import admin
from .models import Genre, Film, Attachment, Artist

admin.site.register(Genre)
admin.site.register(Film)
admin.site.register(Attachment)
admin.site.register(Artist)

