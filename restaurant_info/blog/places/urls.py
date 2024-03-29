from django.contrib import admin 
from django.urls import path 
from .views import home, single_page, user_login, add_comment, test_map
  
urlpatterns = [ 
    path('map', test_map),
    path('places/', home, name='places'),
    path('places/<int:id>',single_page, name='single_page'),
    path('places/<int:id>/comment', add_comment),
    path('accounts/login/', user_login, name='login'),
] 
