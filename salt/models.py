from django.db import models

# Create your models here.

class Member(models.Model):
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=200)
    roles = models.JSONField(default=list)  # Store roles as a list
    quote = models.TextField(blank=True)
    image = models.ImageField(upload_to='salt/images/')
    order = models.IntegerField(default=0, help_text="Order in which to display the member")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'username']

    def __str__(self):
        return self.username
