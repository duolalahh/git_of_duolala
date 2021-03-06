from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.fields import exceptions
from django.utils import timezone

class ReadNum(models.Model):
    read_num=models.IntegerField(default=0)

    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    objects_id=models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type','objects_id')

class ReadNumModel():
    def get_read_num(self):
        ct=ContentType.objects.get_for_model(self)
        try:
            readnum=ReadNum.objects.get(content_type=ct,objects_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0
class ReadDetail(models.Model):
    read_num=models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type','object_id')


# Create your models here.
