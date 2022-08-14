# Register your models here.

# from django.contrib import admin
# from polls.models import Post
# from polls.models import Comment


# admin.site.register(Post)
# admin.site.register(Comment)

from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inline = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

# admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)