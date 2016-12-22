from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^design/01/$', views.design01, name='design01'),
    url(r'^design/02/$', views.design02, name='design02'),
    url(r'^design/03/$', views.design03, name='design03'),
    url(r'^design/04/$', views.design04, name='design04'),
    url(r'^design/05/$', views.design05, name='design05'),
    url(r'^design/06/$', views.design06, name='design06'),
    url(r'^design/07/$', views.design07, name='design07'),
    url(r'^design/08/$', views.design08, name='design08'),
    url(r'^design/09/$', views.design09, name='design09'),
    url(r'^design/10/$', views.design10, name='design10'),
    url(r'^development/01/$', views.development01, name='development01'),
]