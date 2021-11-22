from django.db import models

def upload_image(instance, filename):
    return f'{instance.id}-{filename}'

class ListaModel(models.Model):
    ADQUIRIDO = (
        ("Sim", 'SIM'),
        ("Não", 'NAO',)
    )
    id = models.AutoField(primary_key=True, serialize=True, verbose_name='ID',)
    produto = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    adquirido = models.CharField(max_length=3, choices=ADQUIRIDO, blank=True, null=True)
    imagem = models.ImageField(upload_to=upload_image, blank=True, null=True)

    def __str__(self):
        return self.produto

