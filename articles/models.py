from django.db import models
from django.contrib.auth.models import User
from webproject import settings
from django.urls import reverse
from datetime import date, datetime


class Category(models.Model):                    # model for article category
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):                              # error, but action is worked
        # return reverse('articles:all', args=[str(self.id)])
        return reverse('articles:all')


class Post(models.Model):                         # main model for post
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    pub_data = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='personal')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes')

    def all_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' --- ' + str(self.author)

    def get_absolute_url(self):                              # error, but article is saved
        # return reverse('articles:all', args=[str(self.id)])
        return reverse('articles:all')

