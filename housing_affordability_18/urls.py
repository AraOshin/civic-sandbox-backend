from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
   url(r'^slides/building-permits/(?P<date_filter>.+)/', views.building_permits_layer.get_view()),
   url(r'^slides/building-permits/', views.building_permits_layer.get_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)

