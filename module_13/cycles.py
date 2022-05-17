tickets_count =int(input("Введите количество билетов:"))
price_list = []

for i in range(tickets_count):
    age = int(input("Введите возраст:"))
    if age < 18:
        price_list.append(0)
    elif age > 18 and age < 25:
        price_list.append(990)
    else:
        price_list.append(1390)

if tickets_count > 3:
    print("Стоимость с учетом 10% скидки", sum(price_list) * 0.9)
else :
    print("Стоимость без учета скидки", sum(price_list))




