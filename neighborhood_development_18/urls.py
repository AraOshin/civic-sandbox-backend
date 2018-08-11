from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from civic_sandbox.map_layer_maker import SandboxMaker 


bike_parking_layer = SandboxMaker(
    layer_key = '001',
    )
demolitions_layer = SandboxMaker(
    layer_key = '011',
    )


urlpatterns = [
    url(r'^slides/bikeparking/', bike_parking_layer.get_view()),
    url(r'^slides/demolitions/(?P<date_filter>\d+)', demolitions_layer.get_view()),
    url(r'^slides/demolitions/', demolitions_layer.get_view()),
    # url(r'^registry/', views.registry),
]
urlpatterns = format_suffix_patterns(urlpatterns)

