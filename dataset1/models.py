from django.db import models

# Create your models here.
class taraz(models.Model):
    name_sea=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images_sea/',null=True)
    size_sez=models.IntegerField()
    description=models.TextField()

    def __str__(self):
        return self.name_sea