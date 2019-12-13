# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:10:54 2019

@author: erdemk
"""


#Data Types
#Data Tipleri
tamSayi = 10 			    #integer
karakter = 'a' 			    #char
cumle = "Bu bir cümledir." 	#string
ondalikSayi = 2.5 			#float

'''
Aritmetik Operatorler : 
+ Addition		a + b = 30
- Subtraction		a – b = -10
* Multiplication	a * b = 200
/ Division		b / a = 2
% Modulus		b % a = 0
** Exponent		a**b =10 to the power 20
//			9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
'''
'''
Comparison Operators
Karsilastirma Operatorleri
==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
!=	If values of two operands are not equal, then condition becomes true.	(a != b) is true.
<>	If values of two operands are not equal, then condition becomes true.	(a <> b) is true. This is similar to != operator.
>	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
<	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
>=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
<=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.
'''
'''
String Operatorleri
+	Concatenates (joins) string1 and string2	string1 + string2	
a = "Tea " + "Leaf"
print(a)
RESULT
Tea Leaf

*	Repeats the string for as many times as specified by x	string * x	
a = "Bee " * 3
print(a)
RESULT
Bee Bee Bee

[]	Slice — Returns the character from the index provided at x.	string[x]	
a = "Sea"
print(a[1])
RESULT
e

[:]	Range Slice — Returns the characters from the range provided at x:y.	string[x:y]	
a = "Mushroom"
print(a[4:8])
RESULT
room

in	Membership — Returns True if x exists in the string. Can be multiple characters.	x in string	
a = "Mushroom"
print("m" in a)
print("b" in a)
print("shroo" in a)
RESULT
True
False
True
'''


isim = input()
isim2 = input()


a = 'asdfghjklqwertyui'
a[:5]
a[5:]
a[2:5]
print(a[2])

a = 2
type(a)
b = str(a)
type(b)
b

import random
r = random.randint(0,9)
r



a = 9
b = 9
abdullah = 'abdullah'
if a>b:
    print(a)
    print(str(a)+ ', ' + str(b) + ' den buyuktur ')
elif a == b:
    print(a)
    print(b)
    print(abdullah , ' ve ' , b ,' esittir ')
else:
    print(b)
    print( str(b) + ' ,' + str(a) + 'dan buyuktur')




