from django.urls import path
from api.views.tag.detail import detail
from api.views.tag.list import list

urlpatterns = [
    path('tags', list),
    path('tags/<int:pk>', detail),
]
