from django.contrib import admin
from .models import Measurement
from .models import Variable

admin.site.register(Measurement)
admin.site.register(Variable)
