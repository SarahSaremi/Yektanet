from django.db import models
from rest_framework import serializers


class Advertiser(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'Advertiser {self.name}.'


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = '__all__'


class Ad(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField()
    image_url = models.URLField()
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)  # TODO on delete
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Ad {self.title} by {self.advertiser.name}.'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class BaseStat(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    action_time = models.DateTimeField('action_time')
    user_ip = models.GenericIPAddressField('user IP')


class BaseStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseStat
        fields = '__all__'


class Click(BaseStat):
    def __str__(self):
        return f'{self.ad.title} clicked.'


class View(BaseStat):
    def __str__(self):
        return f'{self.ad.title} viewed.'
