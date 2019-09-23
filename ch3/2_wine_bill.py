# Write a function bill1 which, from the prix of 1 liter of wine, `pu` and the bought wine volume `v` returns the amount of the bill with shipping fees which represent 10% of the order's price.
def bill1(v, pu):
    raw_price = v * pu
    shipping_fees = raw_price * 0.1
    return raw_price + shipping_fees


# Write the same function as bill1, but in that new function, the shipping fees are free if the order's price is greater than 100€.
def bill2(v, pu):
    raw_price = v * pu
    if raw_price >= 100:
        return raw_price
    return raw_price + (raw_price * 0.1)


# Write the same function as bill2, but the shipping fees must at least be 2€ if shipping fees are not free.
def bill3(v, pu):
    raw_price = v * pu
    if raw_price >= 100:
        return raw_price
    shipping_fees = raw_price * 0.1
    if shipping_fees < 2:
        shipping_fees = 2
    return raw_price + shipping_fees


print("bill1(6, 10) = " + str(bill1(6, 10)))
print("bill2(12, 10) = " + str(bill2(12, 10)))
print("bill3(1, 10) = " + str(bill3(1, 10)))

