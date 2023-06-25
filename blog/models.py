from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    publish_date=models.DateTimeField(null=True)
    cerated_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['cerated_date']
        verbose_name ='پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return f"{self.title} - {self.id}"