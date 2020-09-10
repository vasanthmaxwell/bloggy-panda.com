from django.db import models
from django.urls import reverse
from tinymce import HTMLField
from bloggy.utils import unique_slug_generator
from django.db.models.signals import pre_save
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
    slug = models.SlugField(max_length=250,null=True,blank=True)
    meta = models.CharField(max_length=200)
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
            'slug':self.slug
        })

def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Blog)

class Comments(models.Model):
    post = models.ForeignKey(Blog,related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    commenttime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def comcount(self):
        return self.comment.count()

