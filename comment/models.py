from django.db import models
from post.models import Post


class Comment(models.Model):
    owner = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    is_published = models.BooleanField(default=False)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return self.body
