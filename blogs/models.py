from django.db import models

# Create your models here.
class BlogPost(models.Model):
    """博客"""
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        """返回模型的字符串表示"""
        return self.title,self.text
  