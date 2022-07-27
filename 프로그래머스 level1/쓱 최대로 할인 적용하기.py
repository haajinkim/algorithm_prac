shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):

    shop_prices.sort(reverse=True)
    user_coupons.sort(reverse=True)
    for i in range(len(user_coupons)):
        shop_prices[i] = shop_prices[i] - shop_prices[i] * (user_coupons[i] * 0.01)

    return sum(shop_prices)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.