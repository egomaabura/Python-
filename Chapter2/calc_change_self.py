def return_change(change, money, dict):
    dict[money] = change // money
    change = change % money
    return change


change = -1
while change < 0:
    pay = input("投入する金額：")
    price = input("商品の金額：")
    if not (pay.isdecimal() and price.isdecimal()):
        print("整数を入力してください。")
        continue
    
    pay = int(pay)
    price = int(price)
    change = pay - price

    if change < 0:
        print("金額が不足しています。")

change_money_dict = {
    10000: 0,
    5000: 0,
    1000: 0,
    500: 0,
    100: 0,
    50: 0,
    10: 0,
    5: 0,
    1: 0,
}

print(f"お釣りは{change}円です。")

while change > 0:
    if change >= 5000:
        change = return_change(change, 5000, change_money_dict)
    elif change >= 1000:
        change = return_change(change, 1000, change_money_dict)
    elif change >= 500:
        change = return_change(change, 500, change_money_dict)
    elif change >= 100:
        change = return_change(change, 100, change_money_dict)
    elif change >= 50:
        change = return_change(change, 50, change_money_dict)
    elif change >= 10:
        change = return_change(change, 10, change_money_dict)
    elif change >= 5:
        change = return_change(change, 5, change_money_dict)
    else:
        change = return_change(change, 1, change_money_dict)

for k, v in change_money_dict.items():
    print(f"{k}円：{v}枚")