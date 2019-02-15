from django.urls import path

from .views import base

urlpatterns = [
    path('', base.index, name='root'),
    path('explore', base.explore, name='explore'),
    path(r'explore/<item_id>', base.explore, name='explore'),
]
