from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, 'Draft'), (1, 'Posted'))


class Post(models.Model):
    title = models.CharField(max_length=200,
    unique=True)
    slug = models.SlugField(max_length=200, 
    unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
   

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"The title of this post is: {self.title} | written by {self.author}"



class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    name = models.CharField(
        max_length=50
        )
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(
        auto_now_add=True
        )
    approved = models.BooleanField(
        default=False
        )

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'




    