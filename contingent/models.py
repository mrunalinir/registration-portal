from django.db import models

# Create your models here.
class Contingent(models.Model):

    contingent = models.CharField(max_length=200)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    mode = models.CharField(max_length=10, null=True)

    def vmid(self):
        if self.id/10<1:
            self.vmid="VM19C000"+str(self.id)

        elif self.id/10<10:
            self.vmid="VM19C00"+str(self.id)

        elif self.id/10<100:
            self.vmid="VM19C0"+str(self.id)

        else:
            self.vmid="VM19C"+str(self.id)

        return self.vmid
