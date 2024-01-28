# Практический блок: вторая часть.
#### Файлы
- configuration.py  _-  URL и пути запросов._
- request.py _- Отправка запросов для решения задач._
- data.py _- Тела POST-запросов._
- test.py _- Автотест._
- Автотест _- Скриншот._
- README.md _- Инструкция_
- gitignore
# Работа с базой данных.
- Выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).

SELECT c.login, COUNT(o.*) AS order_count
FROM "Couriers" AS c
JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;

- выведи все трекеры заказов и их статусы. Статусы определяются по следующему правилу: Если поле finished == true, то вывести статус 2. Если поле canсelled == true, то вывести статус -1. Если поле inDelivery == true, то вывести статус 1. Для остальных случаев вывести 0

SELECT track,
CASE
WHEN finished = true THEN 2
WHEN cancelled = true THEN -1
WHEN "inDelivery" = true THEN 1
ELSE 0 
END AS status
FROM "Orders";


# Автоматизация теста к API ЯндексСамокат.
1. Клиент создает заказ.
2. Проверяется, что по треку заказа можно получить данные о заказе.
- Для запуска теста должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest
- Тесты написаны на языке Python