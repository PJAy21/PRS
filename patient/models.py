from django.db import models

class Patient(models.Model):
    patID = models.BigAutoField(primary_key=True)
    patName = models.CharField(max_length=200)
    patBDate = models.DateField(null=True)
    patAddress = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.patName