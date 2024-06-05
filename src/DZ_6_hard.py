from datetime import datetime
from typing import List


def product_list_sorter(products: List[dict], category: str = "") -> str | List[dict]:
    """Функция принимает список продуктов(словарей) и необязательный аргумент с указанием категории.
    Возвращает отсортированный список продуктов по убыванию цены в заданной категории.
    Если категория не задана, сортирует для всех продуктов."""
    if not category:
        result_product_list = sorted(products, key=lambda x: x.get("price"), reverse=True)
    else:
        temp_product_list = [product for product in products if product.get("category") == category]
        if temp_product_list:
            result_product_list = sorted(temp_product_list, key=lambda x: x.get("price"), reverse=True)
        else:
            return "Такой категории продуктов не обнаружено! Проверьте введённые данные!"
    return result_product_list


def internet_market(goods: List[dict]) -> dict:
    """Функция принимает список словарей - информации об интернет заказах за опредлённую дату (дата в ISO формате).
    Возвращает словарь с информацией о средней стоимости и количестве заказов за месяц в формате:
    {"YYYY-MM": {"average_order_value": xxx, "order_count": xxx}}.
    """
    # Определяем список дат, фигурирующих в заданном списке. А также определяем результирующий словарь.
    dates_list = []
    result_order_dict = {}
    # Формируем список уникальных фигурирующих дат формата "YYYY-MM"
    for good in goods:
        if datetime.fromisoformat(good.get("date")).strftime("%Y-%m") not in dates_list:
            dates_list.append(datetime.fromisoformat(good.get("date")).strftime("%Y-%m"))
    # Перебираем список дат и получаем отфильтрованные заказы, пришедшиеся на конкретную дату.
    # Определяем временные счётчики общей суммы заказов и количества заказов за месяц.
    for order_date in dates_list:
        temp_total_order_value = 0
        temp_order_count = 0
        temp_list = filter(lambda x: datetime.fromisoformat(x.get("date")).strftime("%Y-%m") == order_date, goods)
        for good in temp_list:
            temp_order_count += 1
            for item in good["items"]:
                temp_total_order_value += item.get("price") * item.get("quantity")
        # Пополняем результирующий словарь полученными данными средней стоимости заказов
        # и количества заказов согласно заданному формату
        # {"YYYY-MM": {"average_order_value": xxx, "order_count": xxx}}.
        result_order_dict.update(
            {
                order_date: {
                    "average_order_value": temp_total_order_value / temp_order_count,
                    "order_count": temp_order_count,
                }
            }
        )
    return result_order_dict
