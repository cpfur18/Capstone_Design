from django.contrib import admin
from note_book_service.models import Prod, Prod_property, Passmark_cpu_info, Passmark_gpu_info

admin.site.register(Prod)
admin.site.register(Prod_property)
admin.site.register(Passmark_cpu_info)
admin.site.register(Passmark_gpu_info)
# Register your models here.
