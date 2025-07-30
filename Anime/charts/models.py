from django.db import models

class Anime(models.Model):
    anime_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=500)
    english_name = models.CharField(max_length=500, blank=True, null=True)
    other_name = models.CharField(max_length=500, blank=True, null=True)
    score = models.CharField(max_length=50, blank=True, null=True)  # Using CharField since it might contain non-numeric values
    genres = models.TextField()
    synopsis = models.TextField()
    Type = models.CharField(max_length=100)
    episodes = models.CharField(max_length=50)  # Using CharField since it might contain "Unknown" or ranges
    aired = models.CharField(max_length=200)
    premiered = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100)
    producers = models.TextField(blank=True, null=True)
    licensors = models.TextField(blank=True, null=True)
    studios = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    rank = models.CharField(max_length=50, blank=True, null=True)
    popularity = models.IntegerField()
    favorites = models.IntegerField()
    scored_by = models.CharField(max_length=50)
    members = models.IntegerField()
    image_url = models.URLField(max_length=500)
    
    # Add these fields for better data management
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['popularity']
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'
        
    @property
    def score_float(self):
        """Convert score to float if possible"""
        try:
            return float(self.score) if self.score else None
        except (ValueError, TypeError):
            return None