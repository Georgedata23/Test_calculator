# Выполнил: Георгий Павлович Мальцев
# Дата выполнения: 30.08.2024
# Дата получения задания: 28.08.2024


def main(example=str(input("Введите пример: "))):
    try:
        list_ex = example.split()  # Разбиваем на числа и операторы, при этом пробелы уходят
        a = list_ex[0]
        b = list_ex[2]
        operator = list_ex[1]
    except:
        return print("throws Exception //т.к. неверный ввод, не забывайте использовать пробелы") # Если при сплите меньше 3 составляющих массива, то выйдет ошибка
    if len(list_ex) != 3:
        return print("throws Exception //т.к. неверное количество символов")  # Отсекаем ввод больше 3 слов/цифр/знаков...
    elif (a.isdigit() == False) or (b.isdigit() == False):
        return print("throws Exception //т.к. используются нецелые числа или другие символы")  # Отсекаем числа с плавающей запятой
    try:
        a_int = int(a)
        b_int = int(b)
    except:
        return print("throws Exception //т.к. используйте целые числа") # Если выходит ошибка, следовательно используются не числа
    if (a_int > 11) or (b_int > 11) or (a_int < 0) or (b_int < 0):
        return print("throws Exception //т.к. числа должны быть от 1 до 10")  # Вводим ограничение на значение чисел
    elif operator not in ['+', '-', '*', '/']:
        return print("throws Exception //т.к. неверно задан оператор, используйте (+-*/)") # Проверяем правильность оператора
    elif "+" == operator: # При сложении
         return print(a_int + b_int)
    elif operator == '-': # При вычетании
        return print(a_int - b_int)
    elif operator == '*':
        return print(a_int * b_int) # При умножении
    elif operator == '/': # Деление целочисленное
         return print(f'{a_int // b_int} - это результат целочисленный(с округлением)')
    else:
        print('Это конец')

main() # Пример работы функции