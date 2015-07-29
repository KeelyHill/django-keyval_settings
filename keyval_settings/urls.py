from django.conf.urls import url
from .views import settings_dict_view

urlpatterns = [
    url(r'^$', settings_dict_view, name='Settings View'),
    url(r'^(?P<key>\w+)/$', settings_dict_view, name='Setting Detail')
]
