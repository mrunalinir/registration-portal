from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=10, blank=True, null=True)
    college = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    mode = models.CharField(max_length=10, null=True)

    def vmid(self):
        if self.id/10<1:
            self.vmid="VM19EA000"+str(self.id)

        elif self.id/10<10:
            self.vmid="VM19EA00"+str(self.id)

        elif self.id/10<100:
            self.vmid="VM19EA0"+str(self.id)

        else:
            self.vmid="VM19EA"+str(self.id)

        return self.vmid
