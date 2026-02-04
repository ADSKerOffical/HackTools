import phonenumbers # pip install phonenumbers
import requests

from phonenumbers import geocoder, carrier, timezone
phone_number = "+79006068279" # Введи сюда номер телефона в формате E.164
parsed_number = phonenumbers.parse(phone_number)

if not phonenumbers.is_valid_number(parsed_number):
  print("Номера не существует или не удалось получить информацию")
else:
  country = geocoder.description_for_number(parsed_number, "ru")
  operator = carrier.name_for_number(parsed_number, "ru")
  numbertype = phonenumbers.number_type(parsed_number)
  
  print(f"Полученная информация об номере {phone_number}:")
  print(f"Страна/Регион: {country}")
  print(f"Оператор: {operator}")
  print(f"Тип номера: {'Неизвестный' if numbertype == 0 else 'Стационарный' if numbertype == 1 else 'Мобильный' if numbertype == 2 else 'Стационарный или Мобильный' if numbertype == 3 else 'Бесплатный для звонящего' if numbertype == 4 else 'Платный' if numbertype == 5 else 'Разделённа оплата' if numbertype == 6 else 'VOIP' if numbertype == 7 else 'Перенаправляемый' if numbertype == 8 else 'Пэйджер' if numbertype == 9 else 'Корпоративный' if numbertype == 10 else 'Номер голосовой почты' if numbertype == 11 else numbertype}")
  print(f"WhatsApp: https://wa.me/{phone_number.replace("+", "")}")
