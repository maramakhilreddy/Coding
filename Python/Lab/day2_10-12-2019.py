def lovesymbol():
	for i in range(6):
		for j in range(7):
			if (i==0 and j%3!=0) or (i==1 and j%3==0) or i-j==2 or i+j==8:
				print("*",end='')
			else:
				print(" ",end='')
		print()


import math
def quadraticequation(a,b,c):
	x1=(-b+math.sqrt(b*b-(4*a*c)))/(2*a)
	x2=(-b-math.sqrt(b*b-(4*a*c)))/(2*a)
	return x1,x2

def qe():
	print("The Notation is ax^2+bx+c=0")
	a=int(input('Enter a value:'))
	b=int(input('Enter b value:'))
	c=int(input('Enter c value:'))
	print('Your expressin is {}x^2+{}x+{}=0'.format(a,b,c))
	if a!=0 and b**2-4*a*c>=0:
		print('Roots are:{}'.format(quadraticequation(a,b,c)))
	else:
		print("Unable to calculate")
		
		
def listoperations(li):
	s=0
	l=0
	mi=li[0]
	ma=li[0]
	for i in li:
		l+=1
		s+=i
		if i<mi: mi=i
		elif i>ma: ma=i
	return l,s,mi,ma
	
#####################################################################################

print("*"*10,'Love Symbol','*'*10)
lovesymbol()

print("*"*10,'Quadratic Equation','*'*10)

qe()
print("*"*10,'List Operation','*'*10)
l=list(map(int,input('Enter a list separated by space:').strip().split(' ')))
v=listoperations(l)
print(f'''The list is {l}
The length of {l} is {v[0]}
The sum of elements in {l} is {v[1]}
The minimum element in {l} is {v[2]}
The maximum element in {l} is {v[3]}''')



l1=list(map(int,input('Enter a list1 separated by space:').strip().split(' ')))
l2=list(map(int,input('Enter a list2 separated by space:').strip().split(' ')))
l=l1[:-1]+l2
print("""The list 1 is {}
The list 2 is {}
The list concat is {}""".format(l1,l2,l))

k=[x for x in range(10)]
print(k)
k=['{}{}'.format(x,y) for x  in range(3) for y in range(3,6)]
print(k)

while True:
	x=input("Enter Your Name:")
	if x[0]=="#":
		continue
	elif x=='done': 
		break
	else:
		print(x)

s='Maram Akhil Reddy'
l=len(s)
v='aeiou'
g=[i for i in s if i in v]
print(g,'The percentage of v in s is %.2f'%(len(g)*100/l))

print("The string contains %s"%("Hello"))


try:
	x=10/0
except ZeroDivisionError:
	print("Divided By Zero Error")
finally:
	print("This is finally block")