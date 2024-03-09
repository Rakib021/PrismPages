from django.contrib import admin
from .models import Category,Post
#for admin panel theme change we used material admin site for django
# https://github.com/MaistrenkoAnton/django-material-admin
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display =('image_tag','title','description','url','add_date')
    search_fields = ('title',)
    
    
class PostAdmin(admin.ModelAdmin):
    list_display= ('post_id','title','cat','url')
    search_fields =('title',)
    list_filter =('cat',)
    
    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)