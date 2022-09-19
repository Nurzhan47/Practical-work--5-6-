#task1
t1 = list(input("Enter the size "))
print(t1[::-1])
print('\n')
#Task2
def change(t2):
    t2[0],t2[len(t2)-1] = t2[len(t2)-1],t2[0]
t2 = [1,2,3]
change(t2)
print(t2)
print("\n")
#task3
def to_list(*t3):
    return list(t3)
print(to_list(5,3,1,2,4,5,7,10,2,57))
print("\n")
#task 4
lxqwe = [1,2,3,4,5,6,7,8]
def uselessNumber(t):
    return max(t)/len(t)
print(uselessNumber(lxqwe))
print("\n")
#task 5

def list_sort(t5):
    return sorted(map(abs, t5), reverse=True)
t5_1 = [1,-2,3,-4,5,-6,7,8,-9,-10]
print(list_sort(t5_1))
print("\n")
#task 6
a = ["HUUUUUGEEEEEE", "litle", "sht"]
print([i.rjust(len(max(a, key = len)), '*') for i in a])
