from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^slides/bike-parking/', views.bike_parking_layer.get_view()),
    url(r'^slides/demolitions/(?P<date_filter>\d+)', views.demolitions_layer.get_view()),
    url(r'^slides/demolitions/', views.demolitions_layer.get_view()),
    url(r'^slides/bike-lanes/', views.bike_lanes_layer.get_view()),
    url(r'^foundations/monthly-camp-reports/(?P<date_filter>\d+)', views.monthly_camp_reports_layer.get_view()),##TODO fix date filter 
    url(r'^foundations/monthly-camp-reports/', views.monthly_camp_reports_layer.get_view()),
    url(r'^slides/parks/', views.parks_layer.get_view()),
    url(r'^slides/multiuse-trails/', views.multiuse_trails_layer.get_view()),
    url(r'^slides/community-gardens/', views.community_gardens_layer.get_view()),
    url(r'^slides/bike-greenways/', views.bike_greenways_layer.get_view()),
    url(r'^slides/rail-stops/', views.rail_stops_layer.get_view()),
    url(r'^slides/retail-grocers/', views.retail_grocers_layer.get_view()),
    url(r'^slides/camp-sweeps/', views.camp_sweeps_layer.get_view()),
    url(r'^slides/camp-reports/', views.camp_reports_layer.get_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)

