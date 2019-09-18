from django.conf.urls import url
from . import views
app_name="Information"

urlpatterns = [
    url(r'^createemp/$',views.createemp,name="createemp"),
    url(r'emplist/$',views.emplist,name="emplist"),
    url(r'^createemp2/$',views.createemp2,name="createemp2"),
    url(r'^update/(?P<pk>[\d]+)',views.update,name="update"),
    url(r'^update/done/(?P<pk>[\d]+)',views.update2,name="update2"),
    url(r'^confdel/(?P<pk>[\d]+)',views.confdel,name="confdel"),
    url(r'^delete/done/(?P<pk>[\d]+)',views.delete,name="delete")
     ]
    