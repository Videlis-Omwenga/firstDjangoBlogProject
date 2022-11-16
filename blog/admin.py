from django.contrib import admin
from .models import Post

# Register your model on the admin after doing migrations (database creation)
admin.site.register(Post)
