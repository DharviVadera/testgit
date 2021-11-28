Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str1 = "123abcjw:,.@! eiw"
>>> print("initial string : ", str1)
initial string :  123abcjw:,.@! eiw
>>> op1 = [0:8]
SyntaxError: invalid syntax
>>> op1 = str1 [0:8]
>>> op2 = str1 [14:]
>>> print ("final string ",op1+op2)
final string  123abcjweiw
>>> 
