N = int(input("size: "))
arr = []
max=float('-inf')
sub=0
for i in range(0,N):
    arr.append(int(input()))
for i in range(0,N):
    if max<=arr[i]:
        max=arr[i]
for i in range(0,N):
    sub+=arr[i]
sub = sub/N
for i in range(0,N):
    if arr[i]==0:
        arr[i]=sub
print(max)
print(arr)
print('\n')

#task2
print('minimum number')
n = int(input("size:"))
arr = []
arr2 = []
arr3=[]
min=float('inf')
for i in range(0,n):
    arr.append(int(input()))
for i in range(0,n):
    if arr[i]>=0:
        arr2.append(arr[i])
    else:
        arr3.append(arr[i])
for i in range(0,n):
   if min>=arr[i]:
        min=arr[i]
print("arr2: ",arr2)
print("arr3: ",arr3)
print("Min value: ",min)
print("Min value index: ",arr.index(min)+1)
print('\n')
#task3
N = int(input("size: "))
arr = []
count = 0
for i in range(0,N):
    arr.append(int(input()))
    if i % 2!=0:
        count+=arr[i]
print(count)
arr1 = [8,1,7,3,4,6,5,23]
for i in range(0,len(arr1)):
    if arr1[i]<15:
        arr1[i]*=2
        print("num with index ",i+1," was change, " ,arr1[i])
    else:
        print("num with index ",i+1," was not change, " ,arr1[i])
print('\n')
#task4
N = int(input("size: "))
arr = []
max=float('-inf')
for i in range(0,N):
    arr.append(int(input()))
for i in range(0,N):
    if max<=arr[i]:
        max=arr[i]
print(max)
print(arr.index(max)+1)

#2)
N = int(input("size: "))
arr = []
arr2 = []
for i in range(0,N):
    arr.append(int(input()))
for i in range(0,N):
    if arr[i]%2!=0:
        arr2.append(arr[i])
print(arr2)
#task5
arr = []
for i in range(0,10):
    arr.append(int(input()))
arr.sort()
print(arr)
print('\n')
#task 6 
arr = []
for i in range(0,10):
    arr.append(int(input()))
s = arr[9]
arr.sort()
s = arr.index(s)
print("All elements less than max index: " , arr[0:s])
print("All elements more than max index: " ,arr[s:10])
print('\n')

#task 7
arr = []
for i in range(0,10):
    arr.append(int(input()))
sum = 0
product = 1
for i in range(0,10):
    if arr[i]==0:
        sum+=arr[i]
    elif arr[i]%2 == 0:
        sum+=arr[i]
    else:
        product*=arr[i]
print(sum)
print(product)

#2)
N = int(input("size: "))
arr = []
temp = []
min=float('inf')
max = float('-inf')
for i in range(0,N):
    arr.append(int(input()))
for i in range(0,N):
    if min>=arr[i]:
        min=arr[i]
    if max<=arr[i]:
        max=arr[i]
temp.append(arr.index(max))
temp.append(arr.index(min))
arr[temp[0]]=min
arr[temp[1]]=max
print(arr)
print('\n')

#Task8
arr = []
for i in range(0,10):
    arr.append(int(input()))
sum = 0
product = 1
for i in range(0,10):
    sum+=arr[i]
    product*=arr[i]
print(sum)
print(product)

#2)
N = int(input("size: "))
arr = []
sub=0
for i in range(0,N):
    arr.append(int(input()))
for i in range(0,N):
    sub+=arr[i]
sub = sub/N
for i in range(0,N):
    if arr[i]==0:
        arr[i]=sub
print(arr)
print('\n')

#task9
N = int(input("size: "))
arr = []
min = float('inf')
for i in range(0,N):
    arr.append(int(input()))
for i in range(0,N):
    arr[i] = abs(arr[i])
    if min > arr[i]:
        min=arr[i]
print(min)
arr.reverse()
print(arr)
print('\n')
#task10
#2)
arr = []
arr2 = []
for i in range (0,15):
    arr.append(int(input()))
print(arr)
for i in range (0,15):
    if arr[i]<10:
        arr2.append(0)
    elif arr[i]>20:
        arr2.append(1)
    else:
        arr2.append(arr[i])
print(arr2)
print('\n')

#task11
N = int(input("size: "))
arr = []
max = float('-inf')
for i in range(0,N):
    arr.append(int(input()))
for  i  in range(0,N):
    if arr[i]%2==0:
        if max<arr[i]:
            max=arr[i]
print(max)
print('\n')
#task12
N = int(input("Enter the size "))
arr = []
min = float('inf')
for i in range(0,N):
    arr.append(int(input()))
for i in range(0,N):
    if arr[i]%2!=0:
        if min>arr[i]:
            min=arr[i]
print(min)

#2)
A =[]
B =[]

print("Enter numbers for list A")
for i in range(0,10):
    A.append(int(input()))
print("Enter numbers for list B")
for i in range(0,10):
    B.append(int(input()))
for i in range(0,10):
    temp[i] = A[i]
    A[i] =B[i]
    B[i]=temp[i]
print("Changed A: ", A)
print("Changed B: ", B)
