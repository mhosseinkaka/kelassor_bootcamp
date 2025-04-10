from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('villa/', include('villa.urls')),
    path('foreign-villa/', include('foreign_villa.urls'))
]
