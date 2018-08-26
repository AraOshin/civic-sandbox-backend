from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^slides/safety-hotline/(?P<date_filter>\d+)', views.safety_hotline_layer.get_view()),
    url(r'^slides/safety-hotline/', views.safety_hotline_layer.get_view()),
    url(r'^slides/sensors/', views.sensors_layer.get_view()),


]
urlpatterns = format_suffix_patterns(urlpatterns)

