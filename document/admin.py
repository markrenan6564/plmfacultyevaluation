from django.contrib import admin
from .models import *

admin.site.register(DocMajorComponent)
admin.site.register(DocSubMajorComponent)
admin.site.register(DocSubMinorComponent)
admin.site.register(DocMinorComponent)
admin.site.register(DocCategory)
admin.site.register(DocCriteria)
admin.site.register(DocSubCriteria)
admin.site.register(Document)

