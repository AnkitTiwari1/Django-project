from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^addpost/$',views.addpost,name="addpost"),
    url(r'^addpost2/$',views.addpost2,name="addpost2"),
    url(r'allposts/$',views.allpost,name="allpost"),
    
]
