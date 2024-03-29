from django.db import models

class Card(models.Model):
    text = models.CharField(max_length=100)
    chosen = models.BooleanField(default=False)
    image = models.ImageField(upload_to='cards', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class Player(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)