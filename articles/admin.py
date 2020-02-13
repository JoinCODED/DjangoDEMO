from django.contrib import admin
from .models import Article, AnotherModel

admin.site.register(Article)
admin.site.register(AnotherModel)