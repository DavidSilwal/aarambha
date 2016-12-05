from django.contrib import admin
from webapp.models import *
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
      fields = ('first_name','last_name','contact_no','designation','image',('email','facebook',),)
      search_fields=('first_name','last_name','designation',)
      list_display = ('first_name','contact_no','email','designation',)
      
class BlogAdmin(admin.ModelAdmin):
    #   fieldsets = (
    #       ("Blog information", {
    #           "fields":('title','text','image','pub_date',)
    #       }),
    #       ("Author Details", {
    #           "classes":("collapse",),
    #           "fields":('author','author_email',),
    #           "description":"Author Details"
    #       }),
    #       )
        
      list_display = ('title','author',)
      
class WorkAdmin(admin.ModelAdmin):
      list_display = ('title','pub_date',)

     
class EventAdmin(admin.ModelAdmin):
      list_display = ('title','event_date','status',)
      
admin.site.register(Member,MemberAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Work,WorkAdmin)
admin.site.register(Event,EventAdmin)
