from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    detalhes = models.TextField()
    image = models.ImageField(upload_to='produtos/')  # Não esqueça de instalar Pillow
    
    def __str__(self):
        return self.nome