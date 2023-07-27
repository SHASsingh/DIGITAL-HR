from django.db import models

# Create your models here.
class Notification(models.Model):
    notificationtext=models.TextField()
    notificationdate=models.CharField(max_length=30)
