from django.db import models

class Article(models.Model):
    """docstring forArticle.models"""
    title = models.CharField(max_length=120)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title


    # def __init__(self, arg):
    #     superArticle,models self).__init__()
    #     self.arg = arg
