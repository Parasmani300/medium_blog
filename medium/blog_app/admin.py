from django.contrib import admin
from blog_app.models import Category,Profile,Post,Status,last_4_posts

# Register your models here.
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Status)
admin.site.register(last_4_posts)