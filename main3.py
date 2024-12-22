HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выход из программы"""

today = []
tomorrow = []
other = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input('Дата выполнения задачи: ')
        if date == 'сегодня':
            print(today)
        elif date == 'завтра':
            print(tomorrow)
        else:
            print(other)
    elif command == "add":
        task = input("Введите название задачи: ")
        date = input('Дата выполнения задачи: ')
        if date == 'сегодня':
            today.append(task)
        elif date == 'завтра':
            tomorrow.append(task)
        else:
            other.append(task)
        print("Задача добавлена")
    elif command == 'exit':
        print("Спасибо за использование! До свидания!")
        break