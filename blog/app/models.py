from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

import datetime

class Post(models.Model):
    title =  models.CharField(max_length=50, default='')
    short_description = models.CharField(max_length=250, default='')
    content = RichTextUploadingField(default='')
    date = models.DateTimeField(default=timezone.now)