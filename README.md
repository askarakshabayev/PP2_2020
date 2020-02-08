Lecture 4
Regex
simple text ---	В точности текст «simple text»

\d{5}	--- Последовательности из 5 цифр
\d --- означает любую цифру {5} — ровно 5 раз
\d\d/\d\d/\d{4}	--- Даты в формате ДД/ММ/ГГГГ (и прочие куски, на них похожие, например 98/76/5432)
\b\w{3}\b	--- Слова в точности из трёх букв \b означает границу слова (с одной стороны буква, а с другой — нет) \w — любая буква, {3} — ровно три раза
[-+]?\d+ ---	Целое число, например, 7, +17, -42, 0013 (возможны ведущие нули) [-+]? — либо -, либо +, либо пусто \d+ — последовательность из 1 или более цифр
-------------------------------------
.	    -- Один любой символ, кроме новой строки \n
\d    -- Любая цифра (ab\d\d - ab34, ab56)
\D    -- Любой символ, кроме цифры
\s	  -- Любой пробельный символ (пробел, табуляция, конец строки и т.п.)
\S	  -- Любой непробельный символ
\w	  -- Любая буква (то, что может быть частью слова), а также цифры и _
\W	  -- Любая не-буква, не-цифра и не подчёркивание
[..]	-- Один из символов в скобках, а также любой символ из диапазона a-b	[0-9][0-9A-Fa-f]
[^..]	-- Любой символ, кроме перечисленных
-----------------------------
^ - Caret
^a	a	1 match
    abc	1 match
    bac	No match
^ab	abc	1 match
    acb	No match (starts with a but not followed by b)
-----------------------------
$ - Dollar
a$	a	1 match
    formula	1 match
    cab	No match
-----------------------------
ma*n	mn	1 match
      man	1 match
      maaan	1 match
      main	No match (a is not followed by n)
      woman	1 match
-----------------------------
\b - Matches if the specified characters are at the beginning or end of a word.

\bfoo	football	Match
      a football	Match
      afootball	No match

foo\b	the foo	Match
      the afoo test	Match
      the afootest	No match
-----------------------------

{n}	Ровно n повторений
{m,n}	От m до n повторений включительно
{m,}	Не менее m повторений
{,n}	Не более n повторений
?	Ноль или одно вхождение, синоним {0,1}
*	Ноль или более, синоним {0,}
+	Одно или более, синоним {1,}

re.search(pattern, string)	-- Найти в строке string первую строчку, подходящую под шаблон pattern;

re.fullmatch(pattern, string) --	Проверить, подходит ли строка string под шаблон pattern;
re.split(pattern, string, maxsplit=0)	Аналог str.split(), только разделение происходит по подстрокам, подходящим под шаблон pattern;

re.findall(pattern, string)	Найти в строке string все непересекающиеся шаблоны pattern;

re.finditer(pattern, string)	Итератор всем непересекающимся шаблонам pattern в строке string (выдаются match-объекты);

re.sub(pattern, repl, string, count=0)	Заменить в строке string все непересекающиеся шаблоны pattern на repl;
--------------------------------
Вывести все числа в строке
import re
string = 'hello 12 hi 89. Test 34'
pattern = '\d+'
result = re.findall(pattern, string) 
print(result)

--------------------------------
import re 

match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12') 
print(match[0] if match else 'Not found') 

match = re.search(r'\d\d\D\d\d', r'Телефон 1231212') 
print(match[0] if match else 'Not found') 


match = re.fullmatch(r'\d\d\D\d\d', r'12-12') 
print('YES' if match else 'NO') 

match = re.fullmatch(r'\d\d\D\d\d', r'Т. 12-12') 
print('YES' if match else 'NO') 


print(re.split(r'\W+', 'Где, скажите мне, мои очки??!')) 


print(re.findall(r'\d\d\.\d\d\.\d{4}', 
                 r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')) 
# -> ['19.01.2018', '01.09.2017'] 

for m in re.finditer(r'\d\d\.\d\d\.\d{4}', r'Дата рождения 13.02.1920, сегодня 08.02.2020'): 
    print('Дата', m[0], 'начинается с позиции', m.start()) 
# -> Дата 19.01.2018 начинается с позиции 20 
# -> Дата 01.09.2017 начинается с позиции 45 

print(re.sub(r'\d\d\.\d\d\.\d{4}', 
             r'DD.MM.YYYY', 
             r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')) 
# -> Эта строка написана DD.MM.YYYY, а могла бы и DD.MM.YYYY 
------------------------------
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
------------------------------
Replace every white-space character with the number 9:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
------------------------------
Print the position (start- and end-position) of the first match occurrence.
The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
# print(x.group())
------------------------------
email example
phone example
^a...s$
------------------------------

Data serialization
Flat vs. Nested data
{"type":"A", "field1":"value1", "field2":"value2"}
{
  "A":
  {"field1": "value1", "field2":"value2"}
}
------------------------------
Serializing text to file
a = {"type":"A", "field1":"value1", "field2":"value2"}
file = open("output.txt", "w")
file.write(repr(a))
file.close()
------------------------------
csv file 
import csv
with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(a)
------------------------------
import json
with open('output.txt', 'r') as f:
    data = f.read()


Lecture 3
List Comprehensions examples
1. 
list1 = [4, 2, 6, 7]
list2 = [8, 4, 12, 14]
list2 = [elem * 2 for elem in list1]
print (list2)

2. Using comprehensions print all prime numbers between 1, 1000
import math

def f(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

res = list(range(1, 1000))
res_prime = [item for item in res if f(item)]
print(res_prime)

3. __iter__ and __next__ methods
* Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.
* The iter() function (which in turn calls the __iter__() method) returns an iterator from them.
list, tuple, dict, set

Examples:
3.1
l = [2, 5, 6, 10]
it = iter(l)
next(it)
next(it)
it.__next__()

3.2
for item in l:
  print(item)
------------------------------
it = iter(l)

while True:
  try:
    element = next(it)
    print(element)
  except StopIteration:
    break
------------------------------
4. Python Generators
Generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. Both yield and return will return some value from a function.

The difference is that, while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.

Differences between Generator function and a Normal function
* Generator function contains one or more yield statement.
* When called, it returns an object (iterator) but does not start execution immediately.
* Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
* Once the function yields, the function is paused and the control is transferred to the caller.
* Local variables and their states are remembered between successive calls.
* Finally, when the function terminates, StopIteration is raised automatically on further calls.

4.1.
------------------------------
# A simple generator function
def generator_exampe():
    n = 1
    print('first print')
    yield n

    n += 1
    print('second print')
    yield n

    n += 1
    print('third print')
    yield n

a = generator_example()
print(next(a))
print(next(a))
------------------------------
def fib():
    a = 1
    b = 1
    while True:
        yield a + b
        a, b = b, a + b

a = fib()
print(next(a))
print(next(a))
------------------------------
Python Generator Expression
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
[x**2 for x in my_list]

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
a = (x**2 for x in my_list)
next(a)

sum(x**2 for x in my_list)
max(x**2 for x in my_list)
-----------------------------
5. Class
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
a = Student("a", "b")
print(a)

methods example
------------------------------

Class
iterator example
------------------------------
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
------------------------------

Lecture 2
tuple, string, dictionaries, files, directories

Tuple (immutable)
my_tuple = ()
my_tuple = (1, 2, 3)
my_tuple = (1, "Hello", 3.4)
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
my_tuple = 3, 4.6, "pp2"
a, b, c = my_tuple # unpacking
my_tuple = ("hello",)  
------------------------
# Access Tuple Elements
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:4])
------------------------
# Concatenation
print((1, 2, 3) + (4, 5, 6))
# Repeat
print(("Repeat",) * 3)

# Methods
my_tuple.count('p')
my_tuple.index('l')

# Tuple Membership Test
print('a' in my_tuple)
print(2 not in my_tuple)
----------------------------------------------
# String
my_string = 'Hello'
my_string = "Hello"
my_string = """
hello world
test"""

# Access character
str[0]
str[2:5]
str[5:-2]
# Strings are immutable
str[3] = 'q' - wrong

# String Membership Test
'hello' in 'hello world'

# Methods
len(str) - length of the string
"TeSt".upper()
"TeSt".lower()
"This will split all words into a list".split()
' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
'Happy New Year'.find('ew')
'Happy New Year'.replace('Happy','Brilliant')
----------------------------------------------
# Dictionaries
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

my_dict.get(key, "ppp")
my_dict[key]
# add item
my_dict[key] = value
# delete item
my_dict.pop(key)

# Methods
clear() - remove all items
items() - list of items
keys() - list of keys
values() - list of values 
----------------------------------------------
a_file = open('1.txt', encoding='utf-8')
# Stream
a_string = a_file.read() - reads whole file
a_string = a_file.readline() - read one line
a_string = a_file.readlines() - list of lines
# File object methods
a_file.name
a_file.encoding
a_file.mode

# Reread data
a_file.seek(position)
a_file.read(10)

# Automatically close file
with open('1.txt', encoding='utf-8') as a_file:
    a_file.seek(17)
    a_character = a_file.read(1)
    print(a_character)

with open("1.txt") as file:
  line_number = 0
  for line in file:
    line_number += 1
    print("{} {}".format(line_number, line.rstrip()))

# Writing to the files
with open("2.txt", mode='w') as file: # mode = 'w', mode = 'a', mode = 'r', mode = 'rb'
  file.write("test")

# Current directory
os.getcwd()
# Getting a Directory Listing
# listdir (returns list)
import os
entries = os.listdir(path_to_folder)

for entry in entries:
  print(entry)
# scandir (returns iterator to file)
with os.scandir("/Users/askar/Desktop") as entries:
  for entry in entries:
    entry.name

# Listing All Files in a Directory
os.path.isfile
os.path.join

basepath = "/Users/askar/Desktop"
for entry in os.listdir(basepath):
  if os.path.isfile(os.path.join(basepath, entry)):
    entry

# List all files in a directory using scandir() and entry.is_file()
basepath = '/Users/askar/Desktop'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)

# Listing directories
entry.is_dir()
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)


# Getting File Attributes
os.scandir returns ScandirIterator
# Getting information about directory or files (size, created date)
info = entry.stat()
info.st_mtime - last modified

with os.scandir("/Users/askar/Desktop") as entries:
  for entry in entries:
    info = entry.stat()
    print(f"{entry.name} - {convert_date(info.st_mtime)}")

# Converting date
from datetime import datetime

def convert_date(timestamp):
  d = datetime.utcfromtimestamp(timestamp)
  formated_date = d.strftime('%d %b %Y')
  return formated_date

# Use previous example
print(f"{entry.name} - {convert_date(info.st_mtime)}")

# Making Directories
os.mkdir()
os.makedirs()

# Simple Filename Pattern Matching Using fnmatch
import os
import fnmatch

with os.scandir("/Users/askar/Desktop") as entries:
  for entry in entries:
    if fnmatch.fnmatch(entry.name, "*.txt"):
      print(entry.name)

# Traversing Directories and Processing Files
os.walk(path, topdown=True)

for dir, dirs, files in os.walk("/Users/askar/Desktop"):
  print(f'Found directory {dir}')
  for file in files:
    print(file)

# Deleting Files and Directories
os.remove(path) - deletes file
os.rmdir(path) - deletes empty directory
shutil.rmtree(path) - delete direcotry tree

# Copy file
src = 'path/to/file.txt'
dst = 'path/to/dest_dir'
shutil.copy(src, dst)

# Copying Directories
shutil.copytree('data_1', 'data1_backup')

# Moving directory
shutil.move('dir_1/', 'backup/')

Lecture 1
1. Python programming language, compiler vs interpreter
2. https://www.python.org/downloads/ - official site for downloading python
3. hello world program, comments, indent (python, python3)
4. input, print, convert data type, + - * / // **
-----------------
a = 5
type(a)

a = 'test'
type(a)
-----------------
Binary	'0b' or '0B'
Octal	'0o' or '0O'
Hexadecimal	'0x' or '0X'
print(0b111)
-----------------
type conversation int(a), str(b)
-----------------
import math
# Output: 3.141592653589793
print(math.pi)

# Output: -1.0
print(math.cos(math.pi))

# Output: 3.0
print(math.log10(1000))

# Output: 720
print(math.factorial(6))

math.gcd(a, b)
------------------
import random
1.
# Output: something in range
print(random.randrange(10,20))

2.
x = ['a', 'b', 'c', 'd', 'e']
# Get random choice
print(random.choice(x))

3.
random.shuffle(x)
print(x)


5. a = input()
   b = input()
   c = a + b

6. several input
   a, b, c = input().split()
7. output format, format output Strings by its positions
8. {:f}, {:d}, {:0.2f}
9. if statement (several examples)
10. loop
    range(), range(start, stop, step)

11. range on list
simple_list = [1, 2, 3]
for i in simple_list:
  i

12. Convert Python range() to List
simple_list = list(range(2, 10, 2))
simple_range = list(reversed(range(0,5)))

13. range on character
wrong:
for i in range('a', 'z'):
  print(i)

correct using ord, chr

14. imports

from itertools import chain
for i in chain(range(10), range(15, 20), range(40,50)):
    print(i)

15. functions 
def function_name(parameters):
	"""docstring"""
	statement(s)
  return value

print(f.__doc__) # docstring

16. list
# empty list
my_list = []
# list of integers
my_list = [1, 2, 3]
# list with mixed datatypes
my_list = [1, "Hello", 3.4]

# nested list
my_list = ["mouse", [8, 4, 6], ['a']]
------------------------
Access by index (my_list[0])
Negative indexing
------------------------
slice lists
my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])
# elements beginning to 4th
print(my_list[:-5])
# elements 6th to end
print(my_list[5:])
------------------------
change or add elements
# mistake values
odd = [2, 4, 6, 8]
# change the 1st item    
odd[0] = 1            
# Output: [1, 4, 6, 8]
print(odd)
# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  
# Output: [1, 3, 5, 7]
print(odd)     
------------------------
append()
odd = [1, 3, 5]
odd.append(7)
# Output: [1, 3, 5, 7]
print(odd)
odd.extend([9, 11, 13])
# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)
------------------------
+ and * operations on list
odd = [1, 3, 5]
# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])
#Output: ["pp2", "pp2", "pp2"]
print(["pp2"] * 3)
------------------------
insert()
odd = [1, 9]
odd.insert(1,3)
# Output: [1, 3, 9] 
print(odd)
odd[2:2] = [5, 7]
# Output: [1, 3, 5, 7, 9]
print(odd)
------------------------
delete
del my_list[2]
del my_list[1:4]
del my_list (after list will be non defined)
------------------------
remove and pop
list = [1, 2, 3, 1, 2, 3]
list.remove(1)
list.pop(2)
------------------------
my_list[2:5] = []
------------------------
sort, reverse, clear
------------------------
List Comprehension
pow2 = [2 ** x for x in range(10)]
all_odd = [x for x in range(1000) if x % 2 == 1]
------------------------
List Membership Test
list = ['aaa', 'bbb', 'ccc']
print('ccc' in list)
------------------------
Iterating Through a List
------------------------

