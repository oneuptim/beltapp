from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register_process$' , views.register_process),
    url(r'^login_process$' , views.login_process),
    url(r'^users/(?P<id>\d+)$' , views.users),
    url(r'^quotes$' , views.quotes),
    url(r'^add_quote$' , views.add_quote),
    # url(r'^add_fav$' , views.add_fav),
    # url(r'^remove_fav$' , views.remove_fav),
    url(r'^logout$', views.logout)

]
