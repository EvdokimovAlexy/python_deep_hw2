# Напишите однострочный генератор словаря,
# который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии
from typing import List

NAMES = ["Алексей Евдокимов", "Вадим Федарчук", "Андрей Сапруненко", "Александр Тарасов"]
STAKE = [10_000, 20_000, 15_000, 30_000]
BONUS = ["10.25%", "15.00%", "6.50%", "12.75%"]


def gen_dict(names: List[str], stake: List[int], bonus: List[str]):
    yield {dictr[0]: dictr[1] for dictr in
           list(map(lambda y: (y[0], y[1] * y[2] / 100), zip(names, stake, map(lambda x: float(x[:-1]), bonus))))}


def main():
    print(NAMES)
    print(STAKE)
    print(BONUS)
    print(*gen_dict(NAMES, STAKE, BONUS))


if __name__ == "__main__":
    main()
