from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.category


class Post(models.Model):
    title = models.CharField(max_length=150, null=False)
    slug = models.SlugField(max_length=150, unique_for_date='publish_date')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    #pic
    publish_date = models.DateTimeField(default=timezone.now)
    categ = models.ForeignKey(Category, on_delete=models.PROTECT)

    #ordering posts descendingly using publish_date
    class Meta:
        ordering = ('-publish_date',)
    def __str__(self):
        return self.title
    