from django.urls import path
from villa.views import (villa_hello, villa_main, 
                    villa_city, test_json, test_file, 
                    test_html, villa_list, villa_city,villa_price,
                    add_villa)


urlpatterns = [
    path('hello', villa_hello),
    path('',villa_main),
    path('test-json', test_json),
    path('note', test_file),
    path('test-html/<str:year>', test_html),
    path('villa-list', villa_list),
    path('city/<str:city_name>', villa_city),
    path('price/<int:selected_price>', villa_price),
    path('add-villa', add_villa),
    path('<str:city_name>', villa_city)
]