# -*- coding: utf-8 -*-
from math import *
import urllib

# thel3l 2016

# Definining Variables I'll need later:

factorial = 1
a = 0
b = 1
yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])
baseURL = 'http://entrar.in/attachments/4/results/'
enrolN = '1'
year = 1
term = 1
termRange = 'I'
yearRange = '2000_2001'
finalURL = 'http://entrar.in/attachments/4/results/'
classI = 1
classS = 'I'

print "Enter '1' to find the area of a square, rectangle or trinagle."
print "Enter '2' to convert between Celsius and Fahrenheit."
print "Enter '3' to find the average of five numbers"
print "Enter '4' to find the largest of three numbers"
print "Enter '5' to DO NOTHING. EMPTY."
print "Enter '6' to figure out if a number is odd or even."
print "Enter '7' to convert days to years."
print "Enter '8' to convert text to ASCII."
print "Enter '9' to identify if a year is a leap year."
print "Enter '10' to identify the type of a character - INT, STR, etc."
print "Enter '11' to find the factorial of a number."
print "Enter '12' to find the roots of a quadratic equation."
print "Enter '13' to identify if a number is prime."
print "Enter '14' to perform all math operations upon two numbers."
print "Enter '15' to find n number of the Fibonacci series."
print "Enter '16' to reverse an entered string."
print "Enter '17' to DO NOTHING. EMPTY."
print "Enter '18' to download and print report cards from entrar.in . Requires Internet Access."
print "Enter '19' to identify if a number is a palindrome."
print "Enter '20' to DO NOTHING. EMPTY."
option = int(input("Enter the program number that you want to run: "))

if option == 1:
	runProgOpt = int(input("Do you want to calcelate the area of a Circle or a Square or a rectangle? If Circle, Enter '1'. Otherwise enter '2': "))
	if runProgOpt == 1:
		radius = int(input("Enter the radius: "))
		print "Area of the circle is = " + str(3.14*radius*radius)
	else:
		side1 = int(input("Enter the length of side 1: "))
		side2 = int(input("Enter the length of side 2: "))
		print "Area of the Square/Rectangle is = "+ str(side2*side1)
elif option == 2:
	convOpt = int(input("Enter '1' to convert from Celsius to Fahrenheit or '2' to convert from Fahrenheit to Celsius: " ))
	if convOpt == 1:
		celsius = int(input("Enter the Celsius value: "))
		print "The Fahrenheit equivalent is" + str((celsius*1.8)+32)
	else:
		fahrenheit = int(input("Enter the Fahrenheit value: "))
		print "The Celsius equivalent is " + str((fahrenheit-32)*0.555)

elif option == 3:
	number1 = int(input("Enter the first number: "))
	number2 = int(input("Enter the second number: "))
	number3 = int(input("Enter the third number: "))
	number4 = int(input("Enter the fourth number: "))
	number5 = int(input("Enter the fifth number: "))
	print "The average is " + str((number1+number2+number+number4+number5)/5)

elif option == 4:
	number1 = int(input("Enter the first number: "))
	number2 = int(input("Enter the second number: "))
	number3 = int(input("Enter the third number: "))
	print str(max(number1, number2, number3)) + " is the largest number"

elif option == 5:
	print("This is way too boring. I'll do this later")

elif option == 6:
	number = int(input("Enter a number: "))
	if number % 2 == 0:
		print "The number is even."
	else:
		print "The number is odd."

elif option == 7:
	days = int(input("Enter the number of days: "))
	print str(days) + " is approximately " + str((days/360)) + "years."

elif option == 8:
	charIn = str(input("Enter the character: "))
	print str(ord(charIn)) + " is the ASCII value."

elif option == 9:
	year = int(input("Enter the year: "))
	if year % 4 == 0:
		if year % 100 != 0:
			print str(year) + " was a leap year."
		else:
			if year % 400 == 0:
				print str(year) + " was a leap year."
		

elif option == 10:
	charac = raw_input("Enter the character to test: ")
	print type(charac)


elif option == 11:
	number = int(input("Enter the number to factorialize: "))
	if number == 0:
		print "The factorial of 0 is 1."
	elif number < 0:
		print "You can't factorialize a negative number."
	else:
		for i in range(1,number+1):
			factorial = factorial*i
		print "The factorial of " + str(number) + " is " + str(factorial)


elif option == 12:
	a = int(input("Enter the coefficient of x^2: "))
	b = int(input("Enter the coefficient of x or of x^1: "))
	c = int(input("Enter the constant term or x^0: "))
	discriminant = int((b*b)-4*a*c)
	firstRoot = int(((-b)+(sqrt((b*b)-4*a*c)))/2*a)
	secondRoot = int(((-b)-(sqrt((b*b)-4*a*c)))/2*a)
	print "The roots of the equation are " + str(firstRoot) + " and " + str(secondRoot)

elif option == 13:
	number = int(input("Enter the number to test: "))
	if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0 and number % 9 != 0:
		print "The number is a prime."
	else:
		print "The numberis not a prime."

elif option == 14:
	inp1 = int(input("Number 1: "))
	inp2 = int(input("Number 2: "))
	operation = int(input("Enter '1' to add, '2' to subtract, '3' to multiply or '4' to divide."))
	if operation == 1:
		print "Their sum is " + str(inp1+inp2)
	elif operation == 2:
		print "Their difference is " + str(inp1-inp2)
	elif operation == 3:
		print "Their product is " + str(inp1*inp2)
	elif operation == 4:
		print "The quotient is " + str(inp1/inp2)

elif option == 15:
	iterations = int(input("How many numbers would you like to find? "))
	for i in range(0,iterations+1):
		a,b = b, a+b
		print b

elif option == 16:
	inputString = raw_input("Enter a string to reverse: ")
	print inputString[::-1]
elif option == 17:
	print " No idea what this Q is. I didn't write it down. Someone please tell me."

elif option == 18:
	finPayload='CmltcG9ydCB1cmxsaWIKaW1wb3J0IGJhc2U2NAojIHRoZWwzbCAyMDE2CgojIERlZmluaW5pbmcg\nVmFyaWFibGVzIEknbGwgbmVlZCBsYXRlcjoKCmZhY3RvcmlhbCA9IDEKYSA9IDAKYiA9IDEKeWVz\nID0gc2V0KFsneWVzJywneScsICd5ZScsICcnXSkKbm8gPSBzZXQoWydubycsJ24nXSkKYmFzZVVS\nTCA9ICdodHRwOi8vZW50cmFyLmluL2F0dGFjaG1lbnRzLzQvcmVzdWx0cy8nCmVucm9sTiA9ICcx\nJwp5ZWFyID0gMQp0ZXJtID0gMQp0ZXJtUmFuZ2UgPSAnSScKeWVhclJhbmdlID0gJzIwMDBfMjAw\nMScKZmluYWxVUkwgPSAnaHR0cDovL2VudHJhci5pbi9hdHRhY2htZW50cy80L3Jlc3VsdHMvJwpj\nbGFzc0kgPSAxCmNsYXNzUyA9ICdJJwpvcHRpb24gPSAxOAoKCmlmIG9wdGlvbiA9PSAxODoKCXBy\naW50ICJUaGlzIHByb2dyYW0gaXMgcHJvdmlkZWQgYXMtaXMgd2l0aG91dCBhbnkgd2FycmFudHkg\nb3IgZ3VhcmFudGVlLiBVc2UgaXQgc29sZWx5IGF0IHlvdXIgb3duIHJpc2suIFRoZSBhdXRob3Ig\nYXNzdW1lcyBubyByZXNwb25zaWJpbGl0eSBmb3IgYW55IGRhbWFnZSBjYXVzZWQgdGhyb3VnaCB0\naGUgdXNlIG9mIHRoaXMgcHJvZ3JhbS4gVGhlIGF1dGhvciB3aWxsIG5vdCBiZSByZXNwb25zaWJs\nZSBmb3IgYW55IGNyaW1lcyB0aGF0IHlvdSBtYXkgY29tbWl0IG9yIHJ1bGVzIHRoYXQgeW91IG1h\neSBicmVhayBpbiB1c2luZyB0aGlzIHByb2dyYW0uIERPIE5PVCBVU0UgVEhJUyBQUk9HUkFNIElG\nIFlPVSBESVNBR1JFRSBXSVRIIFRIRSBBQk9WRSBHVUlERUxJTkVTLiIKCWFncmVlbWVudCA9IHJh\nd19pbnB1dCgiRG8geW91IGFncmVlIHdpdGggdGhlIGFib3ZlIGNvbmRpdGlvbnM/IFt5L25dICIp\nLmxvd2VyKCkKCWlmIGFncmVlbWVudCBpbiB5ZXM6CgkJZW5yb2xOID0gcmF3X2lucHV0KCJQbGVh\nc2UgZW50ZXIgeW91ciBFbnJvbGxtZW50IG51bWJlciB3aXRoIHRoZSBjb3JyZWN0IG51bWJlciBv\nZiB6ZXJvZXM6ICIpCgkJdGVybSA9IGludChpbnB1dCgiUGxlYXNlIGVudGVyIHRoZSB0ZXJtIG51\nbWJlcjsgZWc6IDEgb3IgMjogIikpCgoJCWlmIHRlcm0gPT0gMToKCQkJdGVybVJhbmdlID0gJ0kn\nCgkJZWxpZiB0ZXJtID09IDI6CgkJCXRlcm1SYW5nZSA9ICdJSScKCQllbHNlOgoJCQlwcmludCAi\nUGxlYXNlIGVudGVyIGEgdmFsaWQgdGVybSBudW1iZXIuIgoJCgoJCXllYXIgPSBpbnQoaW5wdXQo\nIkVudGVyIHRoZSB5ZWFyIHRoYXQgeW91IGFyZSBzZWFyY2hpbmcgZm9yOyBlZy0gMjAxNCBvciAy\nMDE1IGV0Yy46ICIpKQoKCQlpZiB5ZWFyID09IDIwMTI6CgkJCXllYXJSYW5nZSA9ICcyMDEyXzIw\nMTMnCgkJZWxpZiB5ZWFyID09IDIwMTM6CgkJCXllYXJSYW5nZSA9ICcyMDEzXzIwMTQnCgkJZWxp\nZiB5ZWFyID09IDIwMTQ6CgkJCXllYXJSYW5nZSA9ICcyMDE0XzIwMTUnCgkJZWxpZiB5ZWFyID09\nIDIwMTU6CgkJCXllYXJSYW5nZSA9ICcyMDE1XzIwMTYnCgkJZWxzZToKCQkJcHJpbnQgIlNvcnJ5\nLiBUaGUgcmVwb3J0cyBmb3IgdGhlIHNlbGVjdGVkIHllYXIgYXJlIG5vdCAoeWV0KSBhdmFpbGFi\nbGUuIgoKCQljbGFzc0kgPSBpbnQoaW5wdXQoIkVudGVyIHlvdXIgZ3JhZGUgZm9yIHdoaWNoIHlv\ndSB3YW50IHRvIHJldHJpZXZlIHJlcG9ydHM7IGVnOiA5LCAxMCwgMTE6ICIpKQoJCWlmIGNsYXNz\nSSA9PSAxOgoJCQljbGFzc1MgPSAnSScKCQllbGlmIGNsYXNzSSA9PSAyOgoJCQljbGFzc1MgPSAn\nSUknCgkJZWxpZiBjbGFzc0kgPT0gMzoKCQkJY2xhc3NTID0gJ0lJSScKCQllbGlmIGNsYXNzSSA9\nPSA0OgoJCQljbGFzc1MgPSAnSVYnCgkJZWxpZiBjbGFzc0kgPT0gNToKCQkJY2xhc3NTID0gJ1Yn\nCgkJZWxpZiBjbGFzc0kgPT0gNjoKCQkJY2xhc3NTID0gJ1ZJJwoJCWVsaWYgY2xhc3NJID09IDc6\nCgkJCWNsYXNzUyA9ICdWSUknCgkJZWxpZiBjbGFzc0kgPT0gODoKCQkJY2xhc3NTID0gJ1ZJSUkn\nCgkJZWxpZiBjbGFzc0kgPT0gOToKCQkJY2xhc3NTID0gJ0lYJwoJCWVsaWYgY2xhc3NJID09IDEw\nOgoJCQljbGFzc1MgPSAnWCcKCQllbGlmIGNsYXNzSSA9PSAxMToKCQkJY2xhc3NTID0gJ1hJJwoJ\nCWVsaWYgY2xhc3NJID09IDEyOgoJCQljbGFzc1MgPT0gJ1hJSScKCQllbHNlOgoJCQlwcmludCAi\nRW50ZXIgYSB2YWxpZCBjbGFzcy4iCgoJCWZpbmFsVVJMID0gYmFzZVVSTCArIHN0cih5ZWFyUmFu\nZ2UpKyAiLyIgICsgc3RyKGNsYXNzUykgKyAiLyIgKyBzdHIodGVybVJhbmdlKSArICJfVEVSTV9C\nRV8iICsgc3RyKGVucm9sTikgKyAiLnBkZiIKCQlyZXBvcnRGaWxlID0gdXJsbGliLnVybHJldHJp\nZXZlKGZpbmFsVVJMLCAicmVwb3J0LnBkZiIpCgkJcHJpbnQgIlRoZSBSZXBvcnQgaGFzIGJlZW4g\nZG93bmxvYWRlZCB0byB0aGUgc2FtZSBkaXJlY3RvcnkgYXMgdGhpcyBwcm9ncmFtLiBQcmludCBp\ndCBhdCB5b3VyIGxlaXN1cmUuIgoJCQoJZWxpZiBhZ3JlZW1lbnQgaW4gbm86CgkJcHJpbnQgIkhh\ndmUgYSBuaWNlIGRheS4iCgllbHNlOgoJCXByaW50ICJQbGVhc2UgZW50ZXIgYSB2YWxpZCBvcHRp\nb24uIgo=\n'
	exec(finPayload.decode("base64"))




elif option == 19:
	number = raw_input("Please enter a number: ")
	if number == number[::-1]:
		print "This number is a palindrome."
	else:
		print "The number is not a palindrome."
# This program is provided as-is, and the author assumes  no responsibility for any illegal activity performed with it. This is provided solely for Educational purposes. 
