from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^slides/bike-parking/', views.bike_parking_layer.get_view()),
    url(r'^slides/demolitions/(?P<date_filter>.+)/', views.demolitions_layer.get_view()),
    url(r'^slides/demolitions/', views.demolitions_layer.get_view()),
    url(r'^slides/bike-lanes/', views.bike_lanes_layer.get_view()),
    url(r'^foundations/monthly-camp-reports/(?P<date_filter>.+)/', views.monthly_camp_reports_layer.get_view()),
    url(r'^foundations/monthly-camp-reports/', views.monthly_camp_reports_layer.get_view()),
    url(r'^slides/parks/', views.parks_layer.get_view()),
    url(r'^slides/multiuse-trails/', views.multiuse_trails_layer.get_view()),
    url(r'^slides/community-gardens/', views.community_gardens_layer.get_view()),
    url(r'^slides/bike-greenways/', views.bike_greenways_layer.get_view()),
    url(r'^slides/rail-stops/', views.rail_stops_layer.get_view()),
    url(r'^slides/retail-grocers/', views.retail_grocers_layer.get_view()),
    url(r'^slides/camp-sweeps/(?P<date_filter>.+)/', views.camp_sweeps_layer.get_view()),
    url(r'^slides/camp-sweeps/', views.camp_sweeps_layer.get_view()),
    url(r'^slides/camp-reports/(?P<date_filter>.+)/', views.camp_reports_layer.get_view()),
    url(r'^foundations/voters-18-25/(?P<date_filter>.+)/', views.voters_18_25_layer.get_view()),
    url(r'^foundations/voters-18-25/', views.voters_18_25_layer.get_view()),
    url(r'^foundations/voters-26-32/(?P<date_filter>.+)/', views.voters_26_32_layer.get_view()),
    url(r'^foundations/voters-26-32/', views.voters_26_32_layer.get_view()),
    url(r'^foundations/voters-33-39/(?P<date_filter>.+)/', views.voters_33_39_layer.get_view()),
    url(r'^foundations/voters-33-39/', views.voters_33_39_layer.get_view()),
    url(r'^foundations/voters-40-49/(?P<date_filter>.+)/', views.voters_40_49_layer.get_view()),
    url(r'^foundations/voters-40-49/', views.voters_40_49_layer.get_view()),
    url(r'^foundations/voters-50-plus/(?P<date_filter>.+)/', views.voters_50_plus_layer.get_view()),
    url(r'^foundations/voters-50-plus/', views.voters_50_plus_layer.get_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

