# Register your models here.

# from django.contrib import admin
# from polls.models import Post
# from polls.models import Comment


# admin.site.register(Post)
# admin.site.register(Comment)

from django.contrib import admin

from .models import Question

admin.site.register(Question)