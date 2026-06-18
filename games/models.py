from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):

    GAME_TYPES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('FPS', 'FPS'),
        ('Racing', 'Racing'),
        ('RPG', 'RPG'),
        ('MOBA', 'MOBA'),
        ('Sports', 'Sports'),
        ('Simulation', 'Simulation'),
        ('Strategy', 'Strategy'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=GAME_TYPES, default='Action')

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_percent = models.PositiveIntegerField(default=0)

    image = models.ImageField(upload_to='games/', blank=True, null=True)

    def final_price(self):
        if self.discount_percent > 0:
            discount = (self.original_price * self.discount_percent) / 100
            return self.original_price - discount
        return self.original_price

    def __str__(self):
        return self.title


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    purchased_at = models.DateTimeField(auto_now_add=True)

    is_installed = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.user.username} - {self.game.title}"

class Wishlist(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')

    def __str__(self):
        return f"{self.user.username} cart {self.game.title}"
class LuckySpin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reward = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
class RewardCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reward = models.CharField(max_length=100)
    code = models.CharField(max_length=30, unique=True)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
class UserSpinCredit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    spins = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.spins} spins"