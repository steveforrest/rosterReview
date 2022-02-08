from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
POINTS = ((500, '500'), (1000, '1000'), (1500, '1500'), (2000, '2000'))
FACTIONS = ((1, 'Space Marine'), (2, 'Orcs'), (3, 'Nids'), (4, 'Adeptus Mechanicus'), (5, 'Chaos'))


class RosterList(models.Model):
    """
    model to save the rosters to
    """
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    points = models.IntegerField(choices=POINTS)
    faction = models.IntegerField(choices=FACTIONS)
    roster = models.TextField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post', null=True, blank=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    Comments = models.ManyToManyField(User, related_name='roster_comments', blank=True)
    Likes = models.ManyToManyField(User, related_name='roster_likes', blank=True)
    Dislikes = models.ManyToManyField(User, related_name='roster_dislikes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ['-createdOn']

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.Likes.count()

    def number_of_dislikes(self):
        return self.Dislikes.count()

    def number_of_comments(self):
        return self.Comments.count()

    # def number_of_comments(self):
    #     return self.numberOfComments.count()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    model used to add comments to posts
    """
    post = models.ForeignKey(RosterList, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    # commenter is a new entry so the name of the person adding the comment can be recorded
    commenter =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author', null=True, blank=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    numberOfLikes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    numberOfDislikes = models.ManyToManyField(User, related_name='comment_dislikes', blank=True)


    class Meta:
        ordering = ['createdOn']

  
