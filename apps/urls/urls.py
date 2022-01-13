from django.urls import path
from .views import UrlCreate, redirect_view, UrlDetail


app_name = 'urls'

urlpatterns = [
    path('create/', view=UrlCreate.as_view(), name='url_create'),
    path('urls/<int:pk>/', view=UrlDetail.as_view(), name='url_detail'),
    path('<str:short_url>/', view=redirect_view, name="redirect"),
]
