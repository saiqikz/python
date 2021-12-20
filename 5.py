# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

rev = int(input("Please enter company's revenue: "))
cost = int(input("Please enter company's costs: "))
while rev > cost:
    print('Company is rentable!')
    rent = int(rev / cost * 100)
    print(f'Rentable of Company is {rent} %')
    emp = int(input('Please input amount of employees: '))
    rent1emp = int((rev - cost) / emp)
    print(f'Revenue for 1 employee is {rent1emp}')
    break
else:
    print('Company is non-rentable!')





