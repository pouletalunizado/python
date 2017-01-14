p = True
q = True
print not (p or not q)

p = True
q = False
print not (p or not q)

p = False
q = True
print not (p or not q)

p = False
q = False
print not (p or not q)

# Question 3
n = 123
#print (n % 10) / 10
#print (n % 100 - n % 10) / 10
#print (n // 10) % 10