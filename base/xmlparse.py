import xml.etree.ElementTree as et
from decimal import Decimal

from kanalservis.settings import USD_CODE


def xmlparsing(xml):
    """
    :param xml: Документ в формате xml, обязательный параметр
    :return: Значение курса доллара из документа xml
    """
    usd = USD_CODE
    root = et.fromstring(xml)

    for child in root.iter('Valute'):
        for valutes in child.attrib.values():
            if usd == valutes:
                for details in child.iter('Value'):
                    return Decimal(details.text.replace(',', '.'))
