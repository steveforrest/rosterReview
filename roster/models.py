from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.


class RosterList(models.Model):
    name = models.CharField('Name Of List', max_length=200, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    points = models.IntegerField()
    faction = models.CharField('Faction', max_length=50, null=False, blank=False)
    roster = models.TextField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    createdOn = models.DateTimeField(auto_now_add=True)
    numberOfComments = models.ManyToManyField(User, related_name='roster_comments')
    numberOfLikes = models.ManyToManyField(User, related_name='roster_likes')
    numberOfDislikes = models.ManyToManyField(User, related_name='roster_dislikes')

    class Meta:
        ordering = ['-createdOn']

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.numberOfLikes.count()
    
    def number_of_dislikes(self):
        return self.numberOfDislikes.count()
    
    def number_of_comments(self):
        return self.numberOfComments.count()

class Comment(models.Model):

    post = models.ForeignKey(RosterList, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True)
    numberOfLikes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    numberOfDislikes = models.ManyToManyField(User, related_name='comment_dislikes', blank=True)

    class Meta:
        ordering = ['createdOn']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'