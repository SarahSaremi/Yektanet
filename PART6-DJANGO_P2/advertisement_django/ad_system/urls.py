from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdsView.as_view(), name='index'),
    path('report/', views.ReportView.as_view(), name='report'),
    path('click/<int:ad_id>/', views.AdRedirectView.as_view(), name='ad_details'),
]
