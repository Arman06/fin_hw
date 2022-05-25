# -*- coding: utf-8 -*-
"""КР-ЗБ-ПИ21-*.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MI4bUXkYFJMMePyKkxE0zfkOFuBAmB0o

#Контрольная работа

# 1.

Напишите **рекурсивную** функцию ```fact```, которая вычисляет факториал заданного числа ```x```.
"""

def fact(x):
    if x == 1 or x == 0:
        return 1
    else:
        return fact(x - 1) * x

fact(3)

"""#2
 Создайте функцию ```filter_even```, которая принимает на вход список целых чисел,  и фильтруя, возвращает список, содержащий только четные числа. Используйте ```filter``` для фильтрации и  ```lambda```.
"""

def filter_even(li):
  return list(filter(lambda x: x % 2 == 0, li))


print(filter_even([1, 2, 3, 4, 5, 6]))

"""#3
Напишите функцию ```square``` ,которая принимает на вход список целых чисел и возвращает список с возведенными в квадрат элементами. Используйте ```map```.
"""

def square(li):
  return list(map(lambda x: x ** 2, li))

print(square([1, 2 ,3]))

"""#4
Напишите функцию бинарного поиска ```bin_search```, которая принимает на вход отсортированный список и элемент. Функция должна возвращать индекс искомого элемента в списке. 

Ввод: 
```
[2,5,7,9,11,17,222] 11
```
Вывод: 
 ```
 4
 ```

Ввод:
```
 [2,5,7,9,11,17,222] 12
```
Вывод:
```
  -1
```
"""

def bin_search(li, element):
  l = 0
  r = len(li) - 1
  while r >= l:
      mid = (r + l) // 2
      if li[mid] > element:
          r = mid - 1
      elif li[mid] < element:
          l = mid + 1
      else:
          return mid
  return -1


print(bin_search([1, 2, 3, 4, 5], 4))

"""#5
Напишите функцию ```is_palindrome``` определяющую,является ли строка палиндромом.
Палиндромами являются текстовые строки, которые одинаково читаются слева направо и справа налево. В строках не учитываются знаки препинания, пробельные символы и цифры; регистр не имеет значения. 

На вход подается строка ```string```.

Выведите YES, если строка является палиндромом и NO иначе.

Запрещается использовать reverse списка - ```list[::-1]``` и функцию ```reversed```.
Чтобы учесть это ограничение, эту задачу рекомендуется решать используя технику решения задач "два указателя". Один указатель читает только символы слева направо, а второй - справа налево.

Примеры:

Ввод 
```
Madam, I'm Adam
``` 
Вывод
```
YES
```
Ввод
```
А роза упала на лапу Азора
``` 
Вывод  
```
YES
```
"""

def is_palindrome(string):
    string = ''.join(filter(lambda x: x.isalpha(), string))
    start = 0
    finish = len(string) - 1
    while start != len(string) // 2:
      if string[start].lower() != string[finish].lower():
        return "NO"
      start += 1
      finish -= 1
    return "YES"

print(is_palindrome("Madam, I'm Adam"))

"""# 6
Написать функцию ```calculate```, которая принимает на вход текстовый файл содержащий строки следующего формата:

Формат файла:
    ```арифметическая операция```    ```целое число #1```    ```целое число #2```\
Разделитель - 4 пробела

Функция должна вернуть 1 строку.
Строка содержит набор из чисел, разделенных запятой. 
После последнего числа запятая не ставится.
Каждое число - результат операции: 
    ```"результирующее целое число"``` = ```"целое число #1"``` применить ```"арифметическая операция"``` ```"целое число #2"```

**Пример входного файла:**

`+    5    4`\
`-    -10449    -7623`\
`**    2    10`

**Пример выходной строки (для примера входного файла выше):**

`9,-2826,1024`

**Допустимые операции:**

`+ (сложение)`\
`- (вычитание)`\
`* (умножение)`\
`// (целочисленное деление) (для этой операции подаются только положительные числа)`\
`% (остаток от деления) (для этой операции подаются только положительные числа)`'\
`** (возведение в степень) (для этой операции подаются только положительные числа)`

Входные числа - только целые.\
Выходные числа - только целые.

[Входной файл для самопроверки.](https://drive.google.com/file/d/1OcqaMTseYffO2JAF_thBJDJ-aqFq9Vxc/view?usp=sharing)

[Выходная строка для самопроверки содержится в файле.](https://drive.google.com/file/d/1IkCn8C6ULuEIngSSpkvI-0cIhDUiIEk9/view?usp=sharing)







"""

OPS = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
       '*': lambda x, y: x * y, '//': lambda x, y: x//y,
       '%': lambda x, y: x % y,  '**': lambda x, y: x ** y}


def load_file(filename):
    file = open(filename, encoding='utf-8')
    data = [line.strip().split('    ') for line in file.readlines()]
    file.close()
    return data


def evaluate(l_number, r_number, op):
    if op in OPS:
        return OPS[op](l_number, r_number)
    else:
        print('Неизвестная операция')


def calculate(path2file):
    data = load_file(path2file)
    operation = 0
    f_operand = 1
    s_operand = 2
    result = []
    for exp in data:
        result.append(str(evaluate(int(exp[f_operand]), int(exp[s_operand]), exp[operation])))
    return ','.join(result)


def main_():
    data = calculate('test_input_file_1.txt')
    print(data)


main_()

"""# 7
Написать функцию ```substring_slice```,которой на вход поступают два текстовых файла.

- Первый файл содержит строки текста.   
 
- Второй файл содержит строки из двух целых неотрицательных чисел.
Первое число в строке всегда меньше или равно второму.
Числа всегда меньше длины соответствующей строки первого файла.
Соответствующей - это значит 1-ая строка из 1-го файла соответствует 1-ой строке из 2-го файла, а 123-я строка из 1-го файла соответствует 123-ей строке из 2-го файла.

- Функция должна вернуть строку, состоящую из подстрок 1-го входного файла.
Подстроки разделены пробелами.
Какие брать подстроки - написано во втором файле.
В конце файла пробела нет.

**Например**
120 строка в 1-ом файле: `JBOljrfkrfjgikenfjerkrkvkfKUGlknc`
120 строка во 2-ом файле: `13 27`
Это значит 120 подстрока в результирующем файле это символы с 13 по 27, включая 13-ый и 27-ой символы.
Не забывайте, что нумерация символов в строке с 0.
Пример требуемой подстроки: `kenfjerkrkvkfKU`
- **Пример 1-го входного файла:**
  ```
QxBpXEeyDWHiuTttWjhFMGTlrCMqpSvrNOQoxUbyiZombbLaYqBHvydPJlvdspwwpgeLNlHMVYrZvPsQkcQgPpierYSahialdXlde
rNsZEKdYYlKKRrYGNWEXTYXOpQqrdGANRfoyeVvRwLVhZDfzKhFQkuSYODIXFLYafnXbxuwqZKQKjSiFZAtSponvmulcjicIDhNaQ
TttSFLqbNkHvOeHSKTTGEEGxwtXImLeCmcKjvsIkIIvvlsUSazNuEsdDYlOljweSubVJxHbSJkBpByFiUCFctgrLKhlYgEWWuDYqx
```

- **Пример 2-го входного файла:**
```
30 84
5 79
70 70
```
- **Пример выходной строки:**
```
vrNOQoxUbyiZombbLaYqBHvydPJlvdspwwpgeLNlHMVYrZvPsQkcQgP KdYYlKKRrYGNWEXTYXOpQqrdGANRfoyeVvRwLVhZDfzKhFQkuSYODIXFLYafnXbxuwqZKQKjSiF b

```

[Пример 1-го входного файла для самопроверки.](https://drive.google.com/file/d/1XlnnBunKfNA2c4so3VKH1kXKvFjOLDAX/view?usp=sharing)

[Пример 2-го входного файла для самопроверки.](https://drive.google.com/file/d/1_gIyNhoSptvlvfA8UOlY60rXDva1fW2G/view?usp=sharing)

[Пример выходной строки для двух файлов выше содержится в этом файле.](https://drive.google.com/file/d/11Lsq1DV8iuMsZ_LPuTj50w5Htq1-95Ys/view?usp=sharing)
"""

def load_file(filename):
    file = open(filename, encoding='utf-8')
    data = [line for line in file.readlines()]
    file.close()
    return data


def substring_slice(path2file_1, path2file_2):
    data_1 = load_file(path2file_1)
    data_2 = load_file(path2file_2)
    result = []
    for line_1, line_2 in zip(data_1, data_2):
        start_index, end_index = map(int, line_2.strip().split())
        result.append(line_1[start_index:end_index + 1])
    return ' '.join(result)


print(substring_slice('test_import_file_2_1.txt', 'test_import_file_2_2.txt'))

"""#8

Написать функцию ```decode_ch```,на вход которой поступает строка.В ней хранится набор химических символов (He, O, H, Mg, Fe, ...). Без пробелов.
Нужно расшифровать химические символы в название химических элементов.Функция должна вернуть строку - расшифровку

Для удобства, прилагается [json файл](https://drive.google.com/file/d/1Uugf4zLRjBx-73RfelroOrf1JlTtpLfi/view?usp=sharing), который ставит в соответствие химическому символу его химическое название.

Как прочитать этот файл в словарь python (dict):
```
periodic_table = json.load(open('periodic_table.json'))
```
- **Пример входной строки:**
```
NOTiFICaTiON
```
-**Пример выходной строки:**
```
АзотКислородТитанФторЙодКальцийТитанКислородАзот
```

Обратите внимание, что, например, "Bi" - это "Висмут", а не "БорЙод".
То есть регистр (заглавные или прописные) букв имеет значение.


"""

import json


def decoded_ch(string_of_elements):
    periodic_table = json.load(open('periodic_table.json', encoding='utf-8'))
    search_index = 1
    result = ''
    while string_of_elements:
        last_ch = string_of_elements[search_index:search_index + 1].isupper()\
            if string_of_elements[search_index:search_index + 1] else True
        if string_of_elements[:search_index] in periodic_table and last_ch:
            result += periodic_table[string_of_elements[:search_index]]
            string_of_elements = string_of_elements[search_index:]
            search_index = 1
        else:
            search_index += 1
    return result


print(decoded_ch('NOTiFICaTiON'))

"""#9

Создайте класс с названием Student.

При инициализации объекта подается два аргумента. Первый - имя студента. Второй - фамилия студента.

1. Создайте три атрибута объекта данного класса:

- *name* имя студента
- *surname* фамилия студента
- *fullname* имя и фамилия студента через пробел
2. Создайте метод для экземпляра класса Student под названием greeting, который при вызове возвращает строку Hello, I am Student
Здесь и далее нужно только написать сам класс. 
3. Добавьте новый атрибут класса под названием grades. При инициализации объекта соответственно добавляется новый аргумент, в котором будет лежать список оценок данного студента, по дефолту равный списку [3,4,5]. Создайте метод под названием mean_grade, который возвращает среднее всех оценок студента (то есть среднее этого атрибута).
4. Сделайте метод is_otlichnik, который возвращает строку YES, если средняя оценок студента больше или равна 4.5 и NO в противном случае.
Примечание: этот метод должен вызывать метод mean_grade внутри себя.
5. На этот раз определим операцию сложения для двух студентов. Пусть такая операция возвращает строку следующего вида: "Name1 is friends with Name2", где Name1 и Name2 - имена первого студента и второго (именно атрибут name). То есть, если создать два экземпляра класса Student, то их сумма должна вернуть вышеописанную строку.
6. Теперь переопределим поведение нашего класса с функцией print. Пусть при вызове функции print от экземпляра класса Student печатается его атрибут fullname.


"""

class Student:
    def __init__(self, name, surname, grades=None):
        self.name = name
        self.surname = surname
        self.fullname = name + ' ' + surname
        if grades is None:
            grades = [3, 4, 5]
        self.grades = grades

    def is_otlichnik(self):
        return 'Yes' if self.mean_grades() >= 4.5 else 'NO'

    def greeting(self):
        return f'Hello, I am {self.fullname}'

    def mean_grades(self):
        return sum(self.grades)/len(self.grades)

    def __add__(self, other):
        return f'{self.name} is friends with {other.name}'

    def __str__(self):
        return self.fullname


def main_1():
    student_1 = Student('Bob', 'Green', [4,5,5])
    student_2 = Student('Steve', 'Brown')
    print(student_1.greeting())
    print(student_2)
    print(student_1.is_otlichnik())
    print(student_1 + student_2)


main_1()

"""#10

Определите  класс исключений ```MyError```,
 который принимает строковое сообщение ```msg``` в качестве параметра при инициализации и также имеет атрибут ```msg```.

Подсказка: Чтобы определить кастомный класс  исключения,нужно создавать класс, унаследованный от ```Exception```.


"""

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)


raise MyError('It is my error, guys')

