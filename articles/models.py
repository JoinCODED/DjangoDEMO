from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50, default="Noob")
    content = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    is_draft = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

class AnotherModel(models.Model):
    pass
