from django.contrib import admin

# Register your models here.
from .models import Register,History,Hospital,Feedback,Test

admin.site.register(Register)
admin.site.register(History)
admin.site.register(Hospital)
admin.site.register(Feedback)
admin.site.register(Test)