#Float precision
a=float(12345678901234567.0)
b=float(12345678901234568.0)


print(a-b)
#the result is 0.0 
#Floats only store 53 bits of information, so you are being affected by round-off.Using integers we solve the problem.

c=12345678901234567
d=12345678901234568

print(c-d)
#result=-1
