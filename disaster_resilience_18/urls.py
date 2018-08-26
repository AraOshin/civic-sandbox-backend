from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^slides/points-of-interest/', views.poi_layer.get_view()),
    url(r'^foundations/shaking/', views.shaking_layer.get_view()),
    url(r'^foundations/liquefaction/', views.liquefaction_layer.get_view()),
    url(r'^foundations/landslide/', views.landslide_layer.get_view()),
    url(r'^foundations/census-response/', views.census_response_layer.get_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

