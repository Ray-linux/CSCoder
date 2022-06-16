from django.db import models
# from tinymce.models import HTMLField
# from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=225)
    thumbnail = models.ImageField(upload_to="thumbnails/", max_length=250, null=True, default=None)
    content = models.TextField()
    # content = RichTextField(blank=True, null= True)
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=50)
    timeStamp = models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.title + ' by ' + self.author   
    
    
    '''
    sno 
    Comment
    user
    post
    parent
    timestamp
    '''