from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class Device(models.Model):
    tag_id = models.CharField("Identificação", max_length=150)
    name  = models.CharField("Nome do ativo", max_length=150)
    #image = models.CharField(max_length=100)
    type = models.CharField("Tipo de equipamento",max_length=150)
    region = models.CharField("Regional", max_length=100)
    local = models.CharField("Unidade", max_length=150)
    team_owner = models.CharField("Equipe responsável", max_length=100)
    address = models.CharField("Endereço", max_length=225, blank=True)
    manufacturer = models.CharField("Fabricante", max_length=150, blank=True)
    supplier = models.CharField("Fornecedor", max_length=150, blank=True)
    serial_number = models.CharField("Número serial", max_length=150, blank=True)
    asset_tag = models.CharField("Patrimônio", max_length=150, blank=True)
    description = models.TextField("Descrição", blank=True)
    observation = models.TextField("Observação", blank=True)
    model = models.CharField("Modelo", max_length=150, blank=True)

    STATUS = (
        (1, 'Novo'),
        (2, 'Pronto'),
        (3, 'Pendente'),
    )
    state_item = models.PositiveSmallIntegerField(
      choices=STATUS,
      default=1,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    lock = models.DateTimeField(null=True)

    def __str__(self):
        return self.tag_id +"  "+ self.name
    
    class Meta:
        verbose_name='Equipamento'
        verbose_name_plural = 'Equipamentos'

class ImageDevice(models.Model):
    image_name = models.CharField("Nome da imagem", max_length=150)
    image_file = models.ImageField(blank=True, upload_to='cards')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, default=1)

    def thumbnail(self):
        if self.image_file:
           # return u'<img src="%s" />' % (self.image_file.url)
            return mark_safe('<img src="{0}" width="150" height="150" />'.format(self.image_file.url))
        else:
            return '(No image)'


    thumbnail.short_description = 'Preview image'

    def __str__(self):
        return str(self.image_file)
    
    class Meta:
        verbose_name='Imagem'
        verbose_name_plural = 'Imagens'



