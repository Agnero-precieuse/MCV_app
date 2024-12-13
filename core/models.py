from django.db import models

from django.db import models

class Evenement(models.Model):
    CATEGORIES_CHOICES = [
        ('SPIRITUAL', 'Spiritualité'),
        ('EDUCATION', 'Éducation'),
        ('COMMUNITY', 'Communauté'),
        ('OTHER', 'Autre'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateTimeField()  # Date de début de l'événement
    date_fin = models.DateTimeField(null=True, blank=True)  # Date de fin de l'événement, facultative
    lieu = models.CharField(max_length=255, blank=True, null=True)  # Lieu facultatif
    categorie = models.CharField(
        max_length=50,
        choices=CATEGORIES_CHOICES,
        default='OTHER'
    )  # Catégorie de l'événement
    image = models.ImageField(
        upload_to='evenements/', 
        blank=True, 
        null=True
    )  # Image associée à l'événement
    est_recurrent = models.BooleanField(default=False)  # Indique si l'événement est récurrent

    def __str__(self):
        return self.titre


class Predications(models.Model):
    titre = models.CharField(max_length=200)
    orateur = models.CharField(max_length=100)
    date = models.DateField()
    video_url = models.URLField(blank=True, null=True)  # Lien vers la vidéo de l'enseignement, si disponible

    def __str__(self):
        return f"{self.titre} - {self.orateur}"
    
class EgliseInfo(models.Model):
    adresse = models.CharField(max_length=200)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    programme_hebdomadaire = models.TextField()
