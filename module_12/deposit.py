# 1.Программа формирует список депозитов,на основе процентных ставок и водимой суммы вклада.
# 2.Программа определяет максимальное значение депозита.

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму вклада:")
money = float(money)
deposit = [money * per_cent['ТКБ'], money * per_cent['СКБ'], money * per_cent['ВТБ'], money * per_cent['СБЕР']]
print("Список депозитов: ", deposit)

max_deposit = max(deposit)
print("Максимальный депозит: ", max_deposit)