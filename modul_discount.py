def apply_discount(price, discount_percent):
    """
    Функция для применения скидки к цене.
    price: исходная цена
    discount_percent: процент скидки (от 0 до 100)
    """
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Скидка должна быть от 0 до 100 процентов")

    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount

    return final_price