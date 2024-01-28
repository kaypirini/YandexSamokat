# Марченко Иван, 12 когорта - Финальный проект. Инженер по тестированию плюс.
import configuration
import requests

# Создание заказа c заданным телом
def create_order(order_body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)

# Запрос на получение информацию о заказе по его трек-номеру
def get_order_info_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str(track_number))