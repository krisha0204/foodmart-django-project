from django.db import models

class food(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    foodgrade = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_images/', null=True, blank=True)

    def __str__(self):
        return self.product
