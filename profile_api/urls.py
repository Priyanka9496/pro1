from django.conf.urls import url
from django.urls import path
from profile_api import views


urlpatterns=[
    url(r'hello-view/',views.HelloApiView.as_view()),
]
