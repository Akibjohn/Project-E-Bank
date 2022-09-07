from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^$',views.index,name="index"),
    re_path(r'^createaccount',views.createaccount,name="createaccount"),
    re_path(r'^create',views.create,name="create"),
    re_path(r'^login',views.login,name="login"),
    re_path(r'^logcode',views.logcode,name="logcode"),
    re_path(r'^depositamt',views.depositamt,name="depositamt"),
    re_path(r'^withdrawamt',views.withdrawamt,name="withdrawamt"),
    re_path(r'^transferamt',views.transferamt,name="transferamt")
    
]