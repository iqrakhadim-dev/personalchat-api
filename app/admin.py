from django.contrib import admin
from .models import User,Category,Personaldetail
# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Personaldetail)