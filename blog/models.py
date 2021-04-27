# from django.db import models
# from django.urls import reverse 
# # Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
#     body = models.TextField()


#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#          # new
#         return reverse('post_detail', args=[(self.id)])

from django.db import models
from django.urls import reverse # new

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
)
    body = models.TextField()
    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
    Post = models.ForeignKey('blog.post', on_delete=models.CASCADE, related_name='comment')
    author  = models.CharField(max_length= 200)
    text = models.TextField()

    def approve(self):
        self.approve_comment = True
        self.save()

    def __str__(self):
        return self.text


