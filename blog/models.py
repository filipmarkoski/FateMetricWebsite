
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from markdown_deux import markdown

# models
from django.db import models
from comments.models import Comment
from django.contrib.auth.models import User


# Create your models here.

# Post.objects.all()
# Post.objects.create(user=user, title="Some time")

class Categories(models.Model):
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category


class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


def upload_location(instance, filename):
    return "%s/%s" % (instance.title, filename)


class Post(models.Model):
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField(max_length=15000, null=True, blank=True)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    post_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

    def get_markdown(self):
        content = self.content
        return mark_safe(markdown(content))

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)
