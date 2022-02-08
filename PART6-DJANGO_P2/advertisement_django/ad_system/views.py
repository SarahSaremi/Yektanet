from datetime import datetime

from django.utils import timezone

from django.db.models import Count
from django.db.models.functions import TruncHour
from django.views.generic import TemplateView

from ad_system.models import Advertiser, Click, View, Ad


class AdsView(TemplateView):
    template_name = 'ad_system/ads.html'
    advertisers = Advertiser.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisers'] = AdsView.advertisers
        return context


class AdDetailsView(TemplateView):
    template_name = 'ad_system/ad_details.html'
    ads = Ad.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReportView(TemplateView):
    template_name = 'ad_system/report.html'

    def get_context_data(self, **kwargs):
        all_clicks = Click.objects
        all_views = View.objects

        click_rate = 0
        if all_views.count() != 0:
            click_rate = all_clicks.count() / all_views.count()

        click_view_diff = find_view_click_difference(all_clicks, all_views)

        click_report = list(all_clicks.values('ad').annotate(action_hour=TruncHour('action_time')).annotate(repeat=Count('action_hour')).values('ad_id', 'action_hour', 'repeat').order_by('ad'))
        view_report = list(all_views.values('ad').annotate(action_hour=TruncHour('action_time')).annotate(repeat=Count('action_hour')).values('ad_id', 'action_hour', 'repeat').order_by('ad'))

        context = super().get_context_data(**kwargs)
        context['click_rate'] = click_rate
        context['click_view_diff'] = click_view_diff
        context['click_report'] = click_report
        context['view_report'] = view_report

        return context


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
