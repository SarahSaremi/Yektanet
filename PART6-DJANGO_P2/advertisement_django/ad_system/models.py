from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Advertiser(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'Advertiser {self.name}.'


class Ad(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField()
    image_url = models.URLField()
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)  # TODO on delete
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Ad {self.title} by {self.advertiser.name}.'


class BaseStat(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    action_time = models.DateTimeField('action_time')
    user_ip = models.GenericIPAddressField('user IP')


class Click(BaseStat):
    def __str__(self):
        return f'{self.ad.title} clicked.'


class View(BaseStat):
    def __str__(self):
        return f'{self.ad.title} viewed.'


class PeriodicReportModel(models.Model):
    click_count = models.IntegerField()
    view_count = models.IntegerField()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


