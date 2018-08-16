from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^slides/bikeparking/', views.bike_parking_layer.get_view()),
    url(r'^slides/demolitions/(?P<date_filter>\d+)', views.demolitions_layer.get_view()),
    url(r'^slides/demolitions/', views.demolitions_layer.get_view()),
    url(r'^slides/bikelanes/', views.bike_lanes_layer.get_view()),
    url(r'^foundations/monthlycampreports/', views.monthly_camp_reports_layer.get_view()),
    url(r'^slides/parks/', views.parks_layer.get_view()),
    url(r'^slides/multiusetrails/', views.multiuse_trails_layer.get_view()),
    url(r'^slides/communitygardens/', views.community_gardens_layer.get_view()),
    url(r'^slides/bikegreenways/', views.bike_greenways_layer.get_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)

