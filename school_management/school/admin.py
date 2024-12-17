from django.contrib import admin
from school.models import User,Student,LibraryHistory,FeesHistory

# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(LibraryHistory)
admin.site.register(FeesHistory)