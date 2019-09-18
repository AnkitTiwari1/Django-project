from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$',views.loginemp,name="login"),
    url(r'^signup/$',views.signup,name="signup"),
    url(r'^logout/$',views.logoutview,name="logout")
]