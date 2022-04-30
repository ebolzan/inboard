from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportMixin

from django import forms
from .models import Device, ImageDevice, User, DevicesProxy

admin.site.site_header  =  "CARBOARD SYSTEM @"
admin.site.site_title  =  "CARBOARD SYSTEM @"
admin.site.index_title = "CadBoard HOME"


class ImageDeviceInstanceInline(admin.TabularInline):
    model = ImageDevice
    readonly_fields = ('thumbnail', 'render_image',)

    def render_image(self, obj):
        #return mark_safe("""<img src="%s" />""" % obj.image_file)
        return mark_safe("""<a href="javascript:window.open('/media/%s','mypopuptitle','width=700,height=500,target=_blank')">open popup</a>""" %obj.image_file)

    class Media:
        css = {
            'all': ('devices/css/style.css',)
        }
        js = ('devices/js/imagelink.js', )


admin.site.register(ImageDevice)


@admin.register(Device)
class DeviceAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('tag_id', 'name','type', 'region', 'local', 'team_owner', 'serial_number', 'asset_tag', 'shorDescription', 'state_item')
    list_per_page = 50
    fieldsets = [('Identificação', {'fields': ['tag_id', 'name', 'type']}),('Localização', {'fields': ['region', 'local', 'team_owner','users', 'address']}), ('Informações', {'fields': ['observation','description', 'serial_number', 'asset_tag', 'model','state_item' ]})]
    inlines = [ImageDeviceInstanceInline]

    def shorDescription(self, obj):
        return obj.observation[:30]

    shorDescription.short_description = 'Descrição'


class DeviceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['device'].label = 'Equipamentos relacionados'


class DeviceInline(admin.TabularInline):
    model = DevicesProxy
    verbose_name_plural = "Equipamentos"
    verbose_name = 'Equipamento'
    form = DeviceForm


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('manager', 'get_all_devices')
    inlines = [DeviceInline,]

    def get_all_devices(self, obj):
        devices = obj.managers.all()
        devices_names = ''
        for device_name in devices:
            devices_names += device_name.name+", "

        return devices_names

    get_all_devices.short_description = 'Equipamentos'
