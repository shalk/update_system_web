from django.contrib import admin

# Register your models here.
from .models import CloudManager,AnsibleAdHoc,BashAdHoc,Files

admin.site.register(CloudManager)
admin.site.register(AnsibleAdHoc)
admin.site.register(Files)
admin.site.register(BashAdHoc)

