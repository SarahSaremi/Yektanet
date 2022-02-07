from django.db import models
from django.utils import timezone


class Advertiser(models.Model):
    advertiser_name = models.CharField(max_length=50)

    def __str__(self):
        return f'Advertiser {self.advertiser_name}.'


class Ad(models.Model):
    ad_title = models.CharField(max_length=100)
    ad_link = models.CharField(max_length=200)
    ad_image_url = models.CharField(max_length=200)
    advertiser_id = models.ForeignKey(Advertiser, on_delete=models.CASCADE) # TODO on delete

    def __str__(self):
        return f'Ad {self.ad_title} by {self.advertiser_id.advertiser_name}.'


class BaseClicksAndView(models.Model):
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    action_time = models.DateTimeField('action_time')
    user_ip = models.GenericIPAddressField('user IP')


class Click(BaseClicksAndView):
    def __str__(self):
        return f'{self.ad.ad_title} clicked.'


class View(BaseClicksAndView):
    def __str__(self):
        return f'{self.ad.ad_title} viewed.'
