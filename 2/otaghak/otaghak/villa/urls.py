from django.urls import path
from .views import villa_hello, villa_main, villa_city, test_json, test_file, test_html


urlpatterns = [
    path('hello', villa_hello),
    path('',villa_main),
    path('test-json', test_json),
    path('note', test_file),
    path('test-html/<str:year>', test_html),
    path('<str:city_name>', villa_city)
]