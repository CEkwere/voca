# Create your models here.
from django.db import models


class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    # Scores for each charism
    capuchin = models.IntegerField(default=0)
    dominican = models.IntegerField(default=0)
    benedictine = models.IntegerField(default=0)
    carmelite = models.IntegerField(default=0)
    augustinian = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class Charism(models.Model):
    """Store the 5 major charisms"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    values = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=7, default="#667eea")
    icon = models.CharField(max_length=50, default="heart")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class CharismDimension(models.Model):
    """Trait/dimension categories (e.g., Simplicity, Contemplative Prayer)"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class CharismScore(models.Model):
    """Score matrix: charism + dimension = score"""
    charism = models.ForeignKey(Charism, on_delete=models.CASCADE, related_name='scores')
    dimension = models.ForeignKey(CharismDimension, on_delete=models.CASCADE, related_name='scores')
    score = models.IntegerField()

    def __str__(self):
        return f"{self.charism.name} - {self.dimension.name}: {self.score}"

    class Meta:
        unique_together = ['charism', 'dimension']
        ordering = ['dimension__order', 'charism__name']