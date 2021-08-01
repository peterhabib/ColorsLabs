from django.db import models

class Data(models.Model):
    Name= models.CharField(max_length=100)
    Age= models.CharField(max_length=100)
    Email= models.CharField(max_length=100)
    Adress= models.CharField(max_length=100)

    def __str__(self):
        return f'{self.Name} - {self.Age} - {self.Email} - {self.Adress}'