# To clear screen in python prompt
import os
os.system('cls')
#print() method
print('print() with \'s')
print("print() with \"s")
print("""print() with \"\"\"s
	this help to display
	paragraph""")


#print() with format and input()
'''
Here input() treats 
default data type as string
'''
print("\n\n\n")
print('*'*10,'Here we can see different ways to use format()','*'*10)
name='Maram Akhil Reddy'	'''input('Enter your name:')	#''' #This is variable declaration
mobile_number=9441761754 #input('Enter your mobile number:')	
print(f'I am {name} and my mobile number is {mobile_number}')
print('I am {} and my mobile number is {}'.format(name,mobile_number))
print('I am {1} and my mobile number is {0}'.format(mobile_number,name))
print('I am {x} and my mobile number is {y}'.format(x=name,y=mobile_number))
print('I am {x} and my mobile number is {y}'.format(y=mobile_number,x=name))




#type() operations
print("\n\n\n")
print('*'*10,'type() operations','*'*10)
print(type(name))
print(type(mobile_number))
#interger
m_n=9441761754
print(type(m_n))
#float
f=5.555
print(type(f))
#boolean
b=True
print(type(b))




#Type casting
print("\n\n\n")
print('*'*10,'Type Casting','*'*10)
#String to int
s='146445'
print('*'*3,'String to int','*'*3)
print(type(s))
i=int(s)
print(type(i))


#String to float
s='56.555446'
print('*'*3,'String to float','*'*3)
print(type(s))
f=float(s)
print(type(f))


#String to boolean
s='True'
print('*'*3,'String to boolean','*'*3)
print(type(s))
b=bool(s)
print(type(b))


#Int to string
i=654654
print(type(i))
s=str(i)
print(type(s))


#Int to float
f=float(i)
print(type(f))


#Int to boolean
i=0
print(type(i))
b=bool(i)
print(type(b))




#Short circuit
print('\n\n\n')
x=2
y=0
if x>3 and x/y>2:
	print("True")
else:
	print("This is short circuit")


#Gardiean Condition
if x>1 and y!=0 and x/y>2:
	print("True")
else:
	print("This is Gardiean Condition")

#String operations
print('\n\n\n')
x='MaramAkhilReddy'
print('*'*10,'String Operations','*'*10)
print('''String is {s}
Length of {s} is {l}
Maximum in {s} is {ma}
Minimum in {s} is {mi}
'''.format(s=x,l=len(x),ma=max(x),mi=min(x)))



#If-else Statements
print('*'*10,'If else statements','*'*10)
x=10
y=20
if True:
	print("This is if block")

if False:
	print("This is if block")
else:
	print("This is else block")

if x>=10:
	print("This is if block")
	if y<=20:
		print("This is nested if block")
	else:
		print("This is else block in nested if")
else:
	print("This is else block")



#Importing statements
print("\n\n\n")
print('*'*10,'Importing','*'*10)
print('*'*3,'Random operations','*'*3)
import random		#Random importing
print(dir(random)) 	#Printing available methods in random

x=random.random()
print(x)

l=[10,20,30,21,423,34]
x=random.choice(l)
print(x)
x=random.choices(l,k=3)
print(x)
for i in range(10):
	x=random.randrange(1,10,2)
	print(x)


print('*'*3,'Math operations','*'*3)
import math
print(dir(math))
x=4
y=math.sqrt(x)
print(y)



#Pattern 
print("\n\n\n")
print('*'*10,'Pattern','*'*10)
for i in range(7):
	for j in  range(6):
		if i+j==6 or j-i==2:
			print('*',end='')
		else:
			print(' ',end='')
	print()
