from datetime import datetime

from django.shortcuts import get_object_or_404
from django.utils import timezone

from django.db.models import Count
from django.db.models.functions import TruncHour
from django.views.generic import TemplateView, RedirectView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ad_system.models import Advertiser, Click, View, Ad
from ad_system.serializers import AdvertiserSerializer, AdSerializer


class AdsView(ListAPIView):
    template_name = 'ad_system/ads.html'
    serializer_class = AdvertiserSerializer
    renderer_classes = [TemplateHTMLRenderer]
    advertisers = Advertiser.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        ads = Ad.objects.all()
        for ad in ads:
            new_view = View(user_ip=self.request.ip_addr, action_time=timezone.now(), ad=ad)
            new_view.save()

        context = {'advertisers': AdsView.advertisers}
        return Response(context)


class AdRedirectView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['ad_id'])
        new_click = Click(ad=ad, action_time=timezone.now(), user_ip=self.request.ip_addr)
        new_click.save()
        return ad.link


class ReportView(ListAPIView):
    template_name = 'templates/ad_system/report.html'
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        all_clicks = Click.objects
        all_views = View.objects

        click_rate = 0
        if all_views.count() != 0:
            click_rate = all_clicks.count() / all_views.count()

        click_view_diff = find_view_click_difference(all_clicks, all_views)

        click_report = list(all_clicks.values('ad').annotate(action_hour=TruncHour('action_time')).annotate(repeat=Count('action_hour')).values('ad_id', 'action_hour', 'repeat').order_by('ad'))
        view_report = list(all_views.values('ad').annotate(action_hour=TruncHour('action_time')).annotate(repeat=Count('action_hour')).values('ad_id', 'action_hour', 'repeat').order_by('ad'))

        context = {'click_rate': click_rate,
                   'click_view_diff': click_view_diff,
                   'click_report': click_report,
                   'view_report': view_report}

        return Response(context)


# ------- ViewSets -------
class AdViewSet(ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class AdvertiserViewSet(ModelViewSet):
    serializer_class = AdvertiserSerializer
    queryset = Advertiser.objects.all()


def find_view_click_difference(all_clicks, all_views):

    diff_sum = 0
    if all_clicks.count() == 0 or all_views.count() == 0:
        return diff_sum

    for click in all_clicks.all():
        related_views = all_views.filter(user_ip=click.user_ip, action_time__lt=click.action_time, ad_id=click.ad_id)
        if related_views.count() != 0:
            view = related_views.order_by('-action_time')[0]
            time_difference = click.action_time - view.action_time
            diff_sum += time_difference.total_seconds()

    average_diff = diff_sum / all_clicks.count()
    average_diff /= 3600
    return average_diff


