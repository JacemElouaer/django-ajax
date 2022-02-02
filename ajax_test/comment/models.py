from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField()

    def __str__(self):
        return self.fullname


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.author

    class Meta:
        ordering = ["-date"]
