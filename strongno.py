x=int(input('enter number: '))
list1=[]
for i in range(1,x):
    if x%i==0:
        list1.append(i)

sum=0
for i in list1:
    sum=sum+i
if sum==x:
    print('strong number')
