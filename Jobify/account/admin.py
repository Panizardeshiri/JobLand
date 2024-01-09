from django.contrib import admin
from .models.accounts import User
from .models.profiles import Profile,ProfileImage,Address,Skill
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email','gender','user_type','created_date','id']
    search_fields = [ 'gender']
    list_filter = ['created_date']
    list_editable= ['user_type','gender']




admin.site.register(ProfileImage)
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Skill)