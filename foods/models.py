from django.db import models

# Create your models here.



def upload_to(instance, filename):
    name,extension =filename.rsplit('.',1)
    return 'photos/%s.%s' % (instance.id,extension)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods')

    def __str__(self):
        return self.name
    