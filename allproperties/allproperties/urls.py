# from django.contrib import admin
# from django.urls import path

# # from allproperties.allproperties import views
# from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('allproperties/', views.allproperties, name='allproperties'),
#     path('buy/', views.buy, name='buy'),
#     path('rent/', views.rent, name='rent'),
#     path('contacus/', views.contacus, name='contacus'),
# ]


from django.contrib import admin
from django.urls import path
from .views import index, allproperties, buy, rent, contactus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('allproperties/', allproperties, name='allproperties'),
    path('buy/', buy, name='buy'),
    path('rent/', rent, name='rent'),
    path('contactus/', contactus, name='contactus'),
]
