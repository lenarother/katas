form django.conf.urls import url

from .views import page


urlpatterns = (
    url(r'^(?<slug>[\w./-]+)/$', page, name='page'),
    url(r'^$', page, name='homepage'),

)
