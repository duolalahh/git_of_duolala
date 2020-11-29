from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumModel,ReadDetail
from django.contrib.contenttypes.fields import GenericRelation


class BlogType(models.Model):
    type_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.type_name
class Blog(models.Model,ReadNumModel):
    blog_type =models.ForeignKey(BlogType,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #read_num=models.IntegerField(default=0)
    read_details =GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Blog: %s>" % self.title 

    class Meta:
        ordering =['-created_time']
