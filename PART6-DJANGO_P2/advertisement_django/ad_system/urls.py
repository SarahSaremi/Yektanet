from django.urls import path
from rest_framework.authtoken import views as auth_views

from . import views

urlpatterns = [
    path('', views.AdsView.as_view(), name='index'),
    path('report/', views.ReportView.as_view(), name='report'),
    path('click/<int:ad_id>/', views.AdRedirectView.as_view(), name='ad_details'),
    # path('api-token-auth/', auth_views.obtain_auth_token)
]
