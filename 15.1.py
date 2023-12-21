"""
2. Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров. Данная промежуточная аттестация
оценивается по системе "зачет" / "не зачет" "Зачет" ставится, если Слушатель успешно выполнил задание.
"Незачет" ставится, если Слушатель не выполнил задание. Критерии оценивания: 1 - Слушатель написал корректный код
для задачи, добавил к ним логирование ошибок и полезной информации.
"""

'''
ДЗ №1.3. простое или составное + логирование ошибок и полезная информация.
Реализована возможность запуска из командной строки с передачей параметров.
'''

import logging
import argparse

# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def user_input_number(message: str, lower_limit: int, upper_limit: int) -> int:
    """Пользовательский ввод."""
    while True:
        try:
            number = int(input(f'{message}'))
            if lower_limit <= number <= upper_limit:
                return number
            else:
                logging.error(
                    f'Число должно быть между {lower_limit} и {upper_limit}')
        except ValueError:
            logging.error('Неверный ввод. Пожалуйста, введите натуральное число.')


def prime_number_test(number: int) -> str:
    """Проверка на простое число."""
    if number in (1, 2):
        return 'Простое число'
    for i in range(2, int(number ** 0.5) + 1):
        if (number % i) == 0:
            return 'Составное число'
    return 'Простое число'


def main(lower_limit: int, upper_limit: int, number: int = None):
    """Основная функция для обработки пользовательского ввода и вывода результата."""
    if number is None:
        message_for_user = f'Пожалуйста, введите натуральное число от {lower_limit} до {upper_limit}: '
        number = user_input_number(message_for_user, lower_limit, upper_limit)
    result = prime_number_test(number)
    print(f'{result} - {number}')
    logging.info(f'{result} - {number}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Проверьте, является ли число простым или составным.')
    parser.add_argument('-n', '--number', type=int,
                        help='Номер для проверки.')
    args = parser.parse_args()

    LOWER_LIMIT = 0
    UPPER_LIMIT = 100000

    if args.number:
        if LOWER_LIMIT <= args.number <= UPPER_LIMIT:
            main(LOWER_LIMIT, UPPER_LIMIT, args.number)
        else:
            logging.error(
                f'Число должно быть между {LOWER_LIMIT} и {UPPER_LIMIT}.')
    else:
        main(LOWER_LIMIT, UPPER_LIMIT)