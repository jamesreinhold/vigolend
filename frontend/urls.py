from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('borrow', views.borrow, name='borrow'),
    path('invest', views.invest, name='invest'),
    path('about-us', views.about_us, name='about_us'),
    path('our-team', views.teams, name='teams')
    # path('', views.index, name='index')
    # path('', views.index, name='index')
]
