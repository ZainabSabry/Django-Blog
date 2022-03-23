from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.category

    def is_subscribed(self):
        return False
    is_subscribed.boolean = True
    is_subscribed.short_description = "Subscription"


#Post
class Post(models.Model):
    title = models.CharField(max_length=150, null=False)
    slug = models.SlugField(max_length=150, unique_for_date='publish_date')
    image = models.ImageField(null=True, blank=True, upload_to='featured_image/%Y/%m/%d/') 
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

    def get_absolute_url(self):
        return reverse('postDetails',args=[self.id])

    tags = TaggableManager()



#Comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_title = models.CharField(max_length=50, null=False)
    comment_body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    proper = models.BooleanField(default=True)

    class Meta:
        ordering = ('create_date',)
    
    def __str__(self):
        return self.comment_title

    # to get child comments in template
    def get_comments(self):
        return Comment.objects.filter(proper=True)


class BlockedWords(models.Model):
    words = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.words