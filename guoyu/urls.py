from django.conf.urls import url, include
from . import views


urlpatterns = [
               #url(r'^a/',views.index),
               url(r'^templist/',views.GetTempList.as_view()),
               url(r'^tempdetail/',views.get_temp_detail),
               ]
