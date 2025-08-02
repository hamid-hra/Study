from django.db import models

class RequestLog(models.Model):
    session_id = models.CharField(max_length=100)
    method = models.CharField(max_length=10)
    headers = models.TextField()
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
