from rest_framework import serializers

from ad_system.models import BaseStat, Ad, Advertiser


class BaseStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseStat
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = '__all__'