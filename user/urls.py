from django.conf.urls import url
from user.views import *
urlpatterns=[
    url(r'^adduser/',adduser,name='adduser'),
    url(r'^deleteuser/',deleteuser,name='deleteuser'),
    url(r'^edituser/',edituser,name='edituser'),
    url(r'^showuser/',showuser,name='showuser'),
]