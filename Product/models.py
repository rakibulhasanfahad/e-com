from django.db import models

# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return str(self.name)

class product(models.Model):
    name = models.CharField(max_length=25)
    pic=models.ImageField(upload_to='prod_pic', null=True, blank=True)
    catagory=models.ForeignKey(Catagory, on_delete = models.CASCADE)
    description=models.TextField()
    price=models.FloatField()
    stock=models.PositiveIntegerField()
    discount_rate=models.PositiveIntegerField()

    def __str__(self):
        return str(self.name)
