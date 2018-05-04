from django.conf.urls import url,include
from master import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [    
    url(r'^$', views.Index_pageview.as_view(), name='index'),
    url(r'^actividades/$', views.Actividades_pageview.as_view(), name='actividades'),
    url(r'^register/$', views.Register_pageview.as_view(), name='register'),
    url(r'^gymbcn/$', views.Gymbcn_pageview.as_view(), name='gymbcn'),
    url(r'^galeria/$', views.Galeria_pageview.as_view(), name='galeria'),
    url(r'^gympass/$', views.Gympass_pageview.as_view(), name='gympass'),
    url(r'^salud/$', views.Salud_pageview.as_view(), name='salud'),
   ]
