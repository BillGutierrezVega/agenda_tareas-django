from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'