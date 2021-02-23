from django.contrib import admin
from .models import Events
from .models import submitEvent

admin.site.register(Events)
admin.site.register(submitEvent)
