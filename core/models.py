from django.db import models
from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Aps(Base):
    ap = models.CharField('AP', max_length=6, primary_key=True)
    modelo = models.CharField('Modelo', max_length=80)
    canal = models.IntegerField('Canal')
    image = StdImageField('Imagem', upload_to='aps', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.ap

def aps_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.ap)


signals.pre_save.connect(aps_pre_save, sender=Aps)
