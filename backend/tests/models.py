from django_clickhouse.models import ClickHouseSyncModel
from django.db import models
# Create your models here.

class UserTest(ClickHouseSyncModel):
    first_name = models.CharField(max_length=50)
    visits = models.IntegerField(default=0)
    birthday = models.DateField()
