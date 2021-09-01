Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6 == 6
True
>>> a = 20; a+= 30; a%=3; print(a)
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False in ‘False’
SyntaxError: invalid character '‘' (U+2018)
>>> ((True == False) or (False > True)) and (False <= True)
False
>>> ##3
>>> s1 = “Nice to have it”
SyntaxError: invalid character '“' (U+201C)
>>> s1 = 'Nice to have it'
>>> s2 = 'here'
>>> s1+s2
'Nice to have ithere'
>>> 
>>> ##4
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a= [3] [2] [1]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a= [3] [2] [1]
IndexError: list index out of range
>>> a [3] [2] [1]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a [3] [2] [1]
TypeError: 'int' object is not subscriptable
>>> a [3] [2] [1]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a [3] [2] [1]
TypeError: 'int' object is not subscriptable
>>> a [3] [1] [2]
['hello']
>>> ##5
>>> a.insert(0,s1)
>>> a.insert(8,s2)
>>> a
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> ##7
>>> color_list_1=set(["white","black","red"])
>>> color_list_2=set(["red","green"])
>>> color_list_1 - color_list_2
{'black', 'white'}
>>> 