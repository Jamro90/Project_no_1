from math import log
a = pow(3,2008)
long(a)
b = pow(4,2019)
long(b)
c = pow(2020,366)
long(c)
if a+b > c:
	print("a+b>c")
if a+b == c:
	print("a+b=c")
if a+b < c:
	print("a+b<c")
print("lewa strona\n" + str(a+b))
print("prawa strona\n" + str(c))
print("logarytm\n" + str(float(log((a+b),2))))
print("logarytm z prawej\n" + str(float(log(c,2))))
