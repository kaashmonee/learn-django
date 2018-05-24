from django.contrib import admin
from .models import Question

# Register your models here.

# We are making the polls app modifiable in the admin
# Otherwise, the admin site would have no idea that the polls app is modifiable
admin.site.register(Question)