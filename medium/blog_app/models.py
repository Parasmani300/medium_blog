from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
from tinymce.models import HTMLField
# Create your models here.
class Category(models.Model):
    topic = models.CharField(max_length=256,unique=True)

    def __str__(self):
        return self.topic

class Status(models.Model):
    post_status = models.CharField(max_length=256,unique=True)

    def __str__(self):
        return self.post_status

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    organisation = models.CharField(max_length=256,default='Learner')
    topic1 = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="topic1")
    topic2 = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="topic2")
    topic3 = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="topic3")
    replacer = models.IntegerField(default=4)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    content = HTMLField()
    author = models.CharField(max_length=256)
    title = models.CharField(max_length=256,default="Title")
    organisation = models.CharField(max_length=256,default='Learner')
    poster = models.ImageField(upload_to='posters',blank=True)
    author_image = models.ImageField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date_created = models.DateField(default=timezone.now())
    editor_choice = models.BooleanField(default=False)
    upvote = models.IntegerField(default=0)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,default='draft')
    

    def __str__(self):
        return self.title

class last_4_posts(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    post1 = models.IntegerField(default=3)
    post2 = models.IntegerField(default=2)
    post3 = models.IntegerField(default=7)
    post4 = models.IntegerField(default=6)

    def __str__(self):
        return self.user.username