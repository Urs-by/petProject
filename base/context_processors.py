from .models import Shop, UserShopRating


def shop_data(request):
    shops = UserShopRating.objects.select_related('shop').all()


    data = [{'name': shop.shop.shop_name, 'latitude': shop.shop.coordinates_lat, 'longitude': shop.shop.coordinates_lng,
             'rating': float(shop.users_rating), 'comment': shop.comment} for shop in shops if
            shop.shop.coordinates_lat and shop.shop.coordinates_lng]
    return {'shop_data': data}
