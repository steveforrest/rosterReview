from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
POINTS = ((500,'500'), (1000,'1000'), (1500, '1500'), (2000, '2000'))
FACTIONS = ((1,'Space Marine'),(2, 'Orcs'),(3,'Nids'),(4, 'Adeptus Mechanicus'),(5,'Chaos'))

class RosterList(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    points = models.IntegerField(choices=POINTS)
    faction = models.IntegerField(choices=FACTIONS)
    roster = models.TextField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    createdOn = models.DateTimeField(auto_now_add=True)
    numberOfComments = models.ManyToManyField(User, related_name='roster_comments', null=True, blank=True)
    numberOfLikes = models.ManyToManyField(User, related_name='roster_likes', null=True, blank=True)
    numberOfDislikes = models.ManyToManyField(User, related_name='roster_dislikes', null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)


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