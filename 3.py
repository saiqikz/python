  # 3. Узнайте у пользователя число n.
  # Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Please input the number: ')
nn = n + n
nnn = n + n + n
n = int(n)
nn = int(nn)
nnn = int(nnn)
s = n + nn + nnn
print(s)