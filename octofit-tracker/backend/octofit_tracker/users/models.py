from django.db import models


# Example user profile model extension (optional placeholder)
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'Profile for {self.user.username}'
