from django.contrib import admin

from blog.admin_models.category import CategoryAdmin
from blog.admin_models.post import PostAdmin
from blog.models import Post, Category

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
