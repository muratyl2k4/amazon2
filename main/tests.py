from django.test import TestCase

from currency_converter import currency_converter
from datetime import date
c = currency_converter.CurrencyConverter()
print(c.convert(100, 'USD', 'TRY' , date=date(2018 , 2 , 2)))
