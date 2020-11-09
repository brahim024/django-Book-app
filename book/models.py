from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
class Post(models.Model):
	post=models.ForeignKey(User,on_delete=models.CASCADE)
class Comment(models.Model):
	posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
	comment_by=models.ForeignKey(Post,on_delete=models.CASCADE)
class Like(models.Model):
	liked_by=models.ForeignKey(User,on_delete=models.CASCADE)
	post=models.ForeignKey(Post,on_delete=models.CASCADE)