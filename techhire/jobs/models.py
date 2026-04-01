from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    MEMBERSHIP_CHOICES = (
        ('basic', 'Basic'),
        ('premium', 'Premium'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    membership = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, default='basic')

    def __str__(self):
        return f"{self.user.username} ({self.membership})"

    @property
    def is_premium(self):
        return self.membership == 'premium'


class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=100)
    application_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()