from django.db import models
#from django.utils import timezone
class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    #create_date = models.DateTimeField(default=timezone.now, help_text="날짜 및 시간")
    create_date = models.DateTimeField(auto_now_add=True)
