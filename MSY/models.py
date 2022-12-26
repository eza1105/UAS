from operator import mod 
from django.db import models
from django.db.models import F 
from django.db.models import Count
import numpy as np
from django.views import *
# Create your models here.

from django.core.validators import FileExtensionValidator

class dataikan(models.Model):
    jenis_usaha    = models.CharField(max_length=50)
    provinsi       = models.CharField(max_length=50)
    jenis_ikan     = models.CharField(max_length=50)
    tahun          = models.IntegerField(null=True)
    trip           = models.FloatField(null=True)#trip adalah ton
    ton            = models.FloatField(null=True)#dan ton adalah trip
    def CPUE (self):
        return self.ton/self.trip
    
class UploadedFile(models.Model):
    name = models.CharField(null=True, max_length=100)
    file = models.FileField(upload_to='static/legenda/', validators=[FileExtensionValidator(allowed_extensions=['zip','rar'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.file.name = self.name
        super().save(*args, **kwargs)


    # def get_intercept(self):
    #     regressor = LinearRegression()
    #     X = dataikan.objects.all().values_list('ton', flat=True).order_by('ton').annotate(CPUE=F('ton')/F('trip')).values('ton').annotate(CPUE=F('CPUE')).values_list('ton', 'CPUE')
    #     Y = dataikan.objects.all().values_list('ton', flat=True).order_by('ton').annotate(CPUE=F('ton')/F('trip')).values('CPUE').annotate(ton=F('ton')).values_list('ton', 'CPUE')
    #     X = np.array(X).reshape(-1, 1)
    #     Y = np.array(Y).reshape(-1, 1)
    #     regressor.fit(X, Y)
    #     return regressor.intercept_