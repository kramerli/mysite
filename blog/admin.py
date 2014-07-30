from django.contrib import admin
from blog.models import *


admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Comment)
# Register your models here.
