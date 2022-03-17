from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
POINTS = ((500, '500'), (1000, '1000'), (1500, '1500'), (2000, '2000'))
FACTIONS = ((1, 'Space Marine'), (2, 'Orcs'), (3, 'Nids'),
            (4, 'Adeptus Mechanicus'), (5, 'Chaos'))


class RosterList(models.Model):
    """
    Save the rosters
    """
    name = models.CharField(max_length=200, unique=True)
    points = models.PositiveSmallIntegerField(choices=POINTS)
    faction = models.PositiveSmallIntegerField(choices=FACTIONS)
    roster = models.TextField(null=False, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='blog_post', null=True,
                                   blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    list_comments = models.ManyToManyField(User,
                                           related_name='roster_comments')
    likes = models.ManyToManyField(User, related_name='roster_likes')
    dislikes = models.ManyToManyField(User, related_name='roster_dislikes')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()

    def number_of_comments(self):
        return self.comments.count()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Adds comments to posts
    """
    post = models.ForeignKey(RosterList, on_delete=models.CASCADE,
                             related_name='comments')
    comment = models.TextField()
    # commenter is a new entry so the name of the person adding the comment
    # can be recorded
    commenter = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='comment_author', null=True,
                                  blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    number_of_likes = models.ManyToManyField(User,
                                             related_name='comment_likes',
                                             blank=True)
    number_of_dislikes = models.ManyToManyField(
                                            User,
                                            related_name='comment_dislikes',
                                            blank=True)

    class Meta:
        ordering = ['-created_on']
