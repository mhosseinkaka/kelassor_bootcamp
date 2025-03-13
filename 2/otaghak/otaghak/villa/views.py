from django.http.response import HttpResponse, JsonResponse, FileResponse
import os
from django.shortcuts import render
from villa.models import Place, Seller
import json
from django.views.decorators.csrf import csrf_exempt



def villa_hello(request):
    return HttpResponse("Hello Kelassor")

def villa_main(request):
    return HttpResponse("This is villa main page!")

def villa_city(request, city_name):
    return HttpResponse(f"Hello {city_name}")

def test_json(request):
    villa_detail = {
        'name' : "Test",
        'city' : 'tehran',
        'no' : '12346548'
    }
    return JsonResponse(villa_detail)


def test_file(request):
    file = os.path.join('/home/saeed/Kelassor/otaghak/otaghak/note.txt')
    return FileResponse(
        open(file, 'rb'),
        as_attachment=True
    )


def test_html(request, year):
    my_data = {
        'year':year,
        'month' : 12
    }
    return render(request, 'villa/main.html', context=my_data)


def villa_list(request):
    my_all_villas = Place.objects.all().order_by("-price").values("title","address","price","id")
    my_all_villas = list(my_all_villas)
    return JsonResponse(my_all_villas ,safe=False)


def villa_city(request, city_name):
    my_all_villas = Place.objects.filter(address=city_name)
    return HttpResponse(my_all_villas)


def villa_price(request, selected_price):
    my_all_villas = Place.objects.filter(price__lte=selected_price)
    # my_all_villas2 = Place.objects.filter(price__gte=selected_price)
    # my_all_villas3 = Place.objects.filter(price__lte=selected_price, price__lte=selected_price)
    # my_all_villas = Place.objects.filter(is_valid=True)
    return HttpResponse(my_all_villas)


@csrf_exempt
def add_villa(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Place.objects.create(
            title=data.get('title'),
            address=data.get('address'),
            price=data.get('price'),
            datetime=data.get('datetime'),
            seller=Seller.objects.get(id=data.get('seller')),
            # seller_id = data.get('seller')
        )
        return HttpResponse("Object Created!")


@csrf_exempt
def delete_villa(request, place_id):
    if request.method == 'DELETE':
        Place.objects.get(id=place_id).delete()
        return HttpResponse("Object Deleted!")


@csrf_exempt
def update_villa(request, place_id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        place = Place.objects.get(id=place_id)
        place.title = data.get('title')
        place.save()
        return HttpResponse("Object Updated!")