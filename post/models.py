from django.db import models
from markitup.fields import MarkupField
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse


class PublishedManager(models.Manager):
    def get_query_set(self):
        return super(PublishedManager, self).get_query_set().filter(
            is_published=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = MarkupField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    objects = models.Manager()
    published_objects = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ("-date_created",)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Image(models.Model):
    post = models.ForeignKey(Post)
    image = models.ImageField(
        upload_to="myblog/static/img", blank=True, null=True)
