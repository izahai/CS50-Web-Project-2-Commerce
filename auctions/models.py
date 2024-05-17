from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    watchlist = models.ManyToManyField('Listing', related_name="watched_by", blank=True)

class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="listings", blank=True, null=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="winning_bids", blank=True, null=True)

    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.title}"
    
class Bid(models.Model):
    dealer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Bid by {self.dealer} on {self.listing} at {self.created_at}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments", null=True)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return f"Comment by {self.user} on {self.listing} at {self.created_at}"

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.category}"
    
    class Meta:
        verbose_name_plural = "Categories"