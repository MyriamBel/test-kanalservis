import requests
from decimal import Decimal
from datetime import datetime

from .models import Supply

from base.xmlparse import xmlparsing
from kanalservis.settings import CURRENCY_URL
from kanalservis.settings import GOOGLE_DOC_NAME, GOOGLE_CELL_SUPPLY, GOOGLE_CELL_ORDER, GOOGLE_CELL_PRICE_USD, \
    GOOGLE_CELL_NUMBER
from base.googlehelper import Gsheet

from kanalservis.settings import BASE_DIR

from django.http import HttpResponse

from django.shortcuts import render


def infotodb(request):

    # Получим текущий курс доллара
    response = requests.get(CURRENCY_URL)
    currency_usd = xmlparsing(response.content)

    # Откроем гугл-документ. Если искомое имя листа не будет найдено, то откроем первый лист.
    gsheet = Gsheet(GOOGLE_DOC_NAME)
    sheet = gsheet.open_sheet_name_or_first()
    records = sheet.get_all_records()

    # Откроем соединение с бд, проверим наличие таблицы. Если она есть, сбросим ее и создадим заново.
    # Затем запишем все строки из гугл-документа в новую таблицу.
    for record in records:
        defaults = {
            'order': record[GOOGLE_CELL_ORDER],
            'price_usd': record[GOOGLE_CELL_PRICE_USD],
            'price_rur': round(Decimal(currency_usd) * record[GOOGLE_CELL_PRICE_USD], 2),
            'supply_date': datetime.strptime(record[GOOGLE_CELL_SUPPLY], '%d.%m.%Y').date().isoformat(),
        }
        obj, created = Supply.objects.update_or_create(
            number_pos=record[GOOGLE_CELL_NUMBER],
            defaults=defaults,
        )

    return HttpResponse("Done")


def index(request):
    supplies = Supply.objects.all().order_by("number_pos")
    total = 0
    for supply in supplies:
        total += supply.price_usd
    context = {'supplies': supplies, 'total': int(total)}
    return render(request, 'kanalservisapp/index.html', context)
