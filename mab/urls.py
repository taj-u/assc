from django.urls import path

from mab.views import home_view
app_name = 'mab'

urlpatterns = [
    path('', home_view, name='home_page')
]
