from django.conf.urls import url
from views import get_lagou, get_zhilian

urlpatterns = [
    url(r'^jobs/get_lagou/$', get_lagou, name='get_lagou'),
    url(r'^jobs/get_zhilian/$', get_zhilian, name='get_zhilian'),
]
