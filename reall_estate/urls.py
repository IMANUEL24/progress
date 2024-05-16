 
from django.contrib import admin
from django.urls import path
from nice.views import listings_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listings_list)
]
