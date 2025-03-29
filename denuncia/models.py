from django.db import models

class Denuncia(models.Model):
    STATUS=(
        ('analysis', 'Em análise'),
        ('archived', 'Arquivada'),
        ('completed', 'Concluída'),
    )

    nome = models.CharField(max_length=255, verbose_name="Nome completo",  blank=False,null=False)
    cpf = models.CharField(max_length=255, verbose_name="CPF",  blank=False,null=False)
    endereco = models.TextField(max_length=255, verbose_name="Endereço completo",  blank=False,null=False)
    descricao = models.TextField(max_length=255, verbose_name="Descricao",  blank=False,null=False)
    celular = models.CharField(max_length=255, verbose_name="Celular",  blank=True,null=True)
    status_denuncia = models.CharField(
        max_length=10, verbose_name="Status", 
         blank=False,null=False, choices=STATUS)
    created_at =models.DateTimeField(auto_now_add= True)
    update_at =models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.descricao
    
    