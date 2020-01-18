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

