from django.contrib import admin
from .models import Question

# Register your models here.

# We are making the polls app modifiable in the admin
# Otherwise, the admin site would have no idea that the polls app is modifiable
# admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    # Splitting form up into field sets
    fieldsets = [
        (None,               {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]})
    ]


# Somehow this makes it show up on the admin page.
# Django is insane, how it is able to so many things out of the box like this
admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)