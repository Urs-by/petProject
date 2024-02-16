from .models import Shop

def shop_data(request):
    shops = Shop.objects.all()
    data = [{'name': shop.shop_name, 'latitude': shop.coordinates_lat, 'longitude': shop.coordinates_lng,
             'rating': float(shop.total_rating)} for shop in shops if shop.coordinates_lat and shop.coordinates_lng]
    return {'shop_data': data}