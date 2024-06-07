from django.db import models


class BaseModel(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=100)
    body = models.TextField()
