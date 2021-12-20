  # 2. Пользователь вводит время в секундах.
  # Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.


sec = int(input('Please enter seconds: '))
min = int(sec / 60)
hour = int(min / 60)

while sec >= 60:
    sec = sec - 60
    continue

while min >= 60:
    min = min - 60
    continue

print(f'{hour}:{min}:{sec}')

