income = [10, 40, 90]


def double_money(dollars):
    return dollars*2
new_income = list(map(double_money, income))
print(new_income)