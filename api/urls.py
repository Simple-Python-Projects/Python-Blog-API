from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.category_views import CategoryList, CategoryDetail
from api.views.tag_views import TagDetail
from api.views.tag_views import TagList

urlpatterns = [
    path('tags', TagList.as_view()),
    path('tags/<int:pk>', TagDetail.as_view()),

    path('categories', CategoryList.as_view()),
    path('categories/<int:pk>', CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
