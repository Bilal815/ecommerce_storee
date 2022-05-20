from django.contrib import admin
from .models import Topic, HelpfulTopic


# Register your models here.
admin.site.register(Topic)
admin.site.register(HelpfulTopic)