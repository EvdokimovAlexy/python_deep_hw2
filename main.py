# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
import math

a = int(input('Введите число стороны "a" в см ='))
b = int(input('Введите число стороны "b" в см ='))
c = int(input('Введите число стороны "c" в см ='))
result = ''
if a > (b + c):
    print('a > (b + c) Такого треугольника не существует')
elif b > (a + c):
    print('b > (a + c) Такого треугольника не существует')
elif c > (a + b):
    print(' c > (a + b) Такого треугольника не существует')
else:
    print('Есть такой треугольник')
if a == b == c:
    print('равносторонний')
elif a == b or a == c or b == c:
    print('равнобедренный')
else:
    print('разносторонний')