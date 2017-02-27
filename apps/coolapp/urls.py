from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register_process$' , views.register_process),
    url(r'^login_process$' , views.login_process),
    url(r'^user/(?P<id>\d+)$' , views.user),
    url(r'^quotes$' , views.quotes),
    url(r'^add_quote$' , views.add_quote),
    url(r'^add_fav/(?P<id>\d+)$' , views.add_fav),
    url(r'^remove_fav/(?P<id>\d+)$' , views.remove_fav),
    url(r'^del_quote/(?P<id>\d+)$' , views.del_quote),
    url(r'^all$' , views.show_all_users),
    url(r'^logout$', views.logout)

]
