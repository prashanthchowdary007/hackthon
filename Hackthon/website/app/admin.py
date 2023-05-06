from django.contrib import admin
from .models import bathroom, bedroom, wardrobe, kitchen, livingroom


# Register your models here.
class ImgAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(bathroom, ImgAdmin)
admin.site.register(bedroom, ImgAdmin)
admin.site.register(wardrobe, ImgAdmin)
admin.site.register(kitchen,  ImgAdmin)
admin.site.register(livingroom, ImgAdmin)
