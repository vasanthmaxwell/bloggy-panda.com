from django.db import models
from django.urls import reverse
from tinymce import HTMLField
# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
class Tags(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Categories)
    overview = models.TextField()
    content = HTMLField()
    authorname = models.CharField(max_length=50)
    authdesc = models.TextField()
    authorimg = models.ImageField()
    image = models.ImageField()
    publishdate = models.DateField()
    tags = models.ManyToManyField(Tags)
    timestamp = models.DateTimeField(auto_now_add=True)
    mintoread = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog-full',kwargs={
            'id':self.id
        })

