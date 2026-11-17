def apply_discount(total):
    """Принимает сумму заказа (число), возвращает сумму заказа со скидкой."""
    if total >= 5000:
        rate = 0.10
    elif total >= 3000:
        rate = 0.05
    else:
        rate = 0
    return round(total * (1 - rate), 2)