from django.http import JsonResponse

from .models import Coupon


def api_can_use(request):
    json_response = {}

    coupon_code = request.GET.get('api/coupon_code', '')

    try:
        coupon = Coupon.objects.get(code=coupon_code)

        if coupon.can_use():
            json_response = {'amount': coupon.value}
        else:
            json_response = {'amount': 0}
    except Exception as e:
        json_response = {'amount': 0}
        print(e, "FROM: coupons")

    return JsonResponse(json_response)
