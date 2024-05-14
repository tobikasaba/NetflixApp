from django.db import models
from tastypie.resources import ModelResource
from netflix.models import Netflix

# Create your models here.


class NetflixResource(ModelResource):
    class Meta:
        queryset = Netflix.objects.all()
        resource_name = "netflix"
