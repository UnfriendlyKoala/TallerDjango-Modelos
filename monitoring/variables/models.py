from django.db import models

class Variable(models.Model):
    name = models.CharField(max_length=50)

    def _str_(self):
        return '{}'.format(self.name)