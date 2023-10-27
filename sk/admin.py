from django.contrib import admin
from .models import data
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
 list_display=("work","name","d_no","s_name","city","district","mobile_no","mobile_no2","mail_id","issue",)

admin.site.register(data,MemberAdmin)


#superuser ..user name = admin
#            pass word = 1234