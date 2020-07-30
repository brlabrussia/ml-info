import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Lender


@csrf_exempt
@require_POST
def cbr(request):
    items = json.loads(request.body)
    for item in items:
        lender = Lender(
            scraped_from=['https://www.cbr.ru/vfs/finmarkets/files/supervision/list_MFO.xlsx'],
            name=item.get('name', ''),
            full_name=item.get('full_name', ''),
            is_legal=True,
            type=item.get('mfo_type', ''),
            regdate=item.get('registry_date', ''),
            regnum=item.get('reg_number'),
            ogrn=item.get('ogrn'),
            inn=item.get('inn'),
            website=item.get('url', ''),
            address=item.get('address', ''),
        )
        lender.save()
    return HttpResponse(status=201)
