# Телеграм-бот калькулятор 

## Описание проекта:
Проект представляет собой телеграм-бот калькулятор для расчета рациональных и комплексных чисел, с возможностью отправлять пользователю ссылку на github.com, где размещен проект и логированием операций.
Основные функции бота прописаны в отдельных модулях.


Запуск производится из файла bot.py. Основные команды:

/start - выводится приветствие и подсказка по дальнейшей работе

/help - выводятся подсказки по доступным командам бота

/calc - после данной команды предлагается выбрать калькулятор рациональных или комплексных чисел

/rational - предлагается ввести рациональное выражение одной строкой для дальнейшего расчета и вывода результата. Выражение расчитывается с учетом приоритетов знаков математических операций и наличия скобок, также  обрабатывается на пробелы (удаляются автоматически) и ошибки (при неверном вводе выводится сообщение о некорректном вводе)

/complex - предлагается ввести комплексное выражение для дальнейшего расчета и вывода результата. Реализовано при помощи встроенной функции eval

/log - в чат отправляется файл с расширением ".txt", где зафиксированы все действия бота с указанием времени (начало работы, выбор команды, введенное выражение и результат/сообщение о неккоректном вводе, отправка лога, получение ссылки на проект в github.com)

/git - отправляется действующая ссылка на проет размещенный на github.com

Примеры работы телеграмм-бота:
![1](https://user-images.githubusercontent.com/111271270/207036918-e94476ab-c380-4286-a233-5b00d3012316.jpg)
![2](https://user-images.githubusercontent.com/111271270/207036948-9561e645-f3e7-4fd8-93f0-81aca0c0af11.jpg)
