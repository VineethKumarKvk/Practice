a=[]
for i in range(1,101):
    a.append(i)

print(list(filter(lambda b:b%2==0,a)))
