from datetime import datetime as dt


def cal_log(expression, result):
    time = dt.now().strftime("%d.%m.%Yг. %H:%M")
    with open('log.txt', 'a') as file:
        file.write(f'Выражение: {expression}. Результат: {result}. Дата запроса: {time}\n')

def act_log(action):
    time = dt.now().strftime("%d.%m.%Yг. %H:%M")
    with open('log.txt', 'a') as file:
        file.write(f'{action}. Время: {time}\n')