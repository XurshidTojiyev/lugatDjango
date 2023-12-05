from django.contrib import admin
from django.urls import path, include
from lugat import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lugat.urls'))
]
