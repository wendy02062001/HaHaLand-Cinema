from django.db import models

# Create your models here.
class Item(models.Model):
    maSP = models.AutoField(primary_key=True)
    tenSP = models.CharField(max_length=20)
    giaBan = models.FloatField()
    hinhAnh = models.TextField()
    available = models.BooleanField()
    moTa = models.TextField()
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.tenSP