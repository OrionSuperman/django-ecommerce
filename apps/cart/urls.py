from django.conf.urls import patterns, url
from . import views
urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^add/$', views.add_to_cart, name='add-to-cart'),
  url(r'^remove/$', views.remove_from_cart, name='remove-from-cart'),
)
