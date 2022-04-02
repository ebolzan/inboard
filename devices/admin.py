from django.contrib import admin
from django.utils.html import format_html

from .models import Device, ImageDevice


class ImageDeviceInstanceInline(admin.TabularInline):
    model = ImageDevice

    readonly_fields = ('thumbnail',)

    class Media:
        css = {
            'all': ('devices/css/style.css',)
        }



admin.site.register(ImageDevice)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('tag_id', 'name', 'type', 'region', 'local', 'team_owner', 'serial_number', 'asset_tag', 'shorDescription')
    inlines = [ImageDeviceInstanceInline]

    def shorDescription(self, obj):
        return obj.observation[:30]

    shorDescription.short_description = 'Descrição'



# Register your models here.
