stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
computed_v = {f'Total price for all {i}s in stock': prices.get(i)*stock.get(i) for i in stock and prices}
print(computed_v)

