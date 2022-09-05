#from django.contrib.auth.models import get_user_model
from config import settings
from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pk}] {self.title}'
