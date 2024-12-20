from this import d
from zipapp import create_archive
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def comment_count(self):
        return self.commentpost_set.all().count()
    
    def comments(self):
        return self.commentpost_set.all()

    def __str__(self) :
        return self.title

class CommentPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)

