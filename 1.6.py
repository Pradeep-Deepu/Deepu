lst= []
n=int(input("Enter the number of elements in the list:"))
for i in range(0,n):
    elements= int(input())
    lst.append(elements)
print("Your list is:",lst)
sum=0
mul=1
for num in lst:
    sum+=num
    mul=mul*num
print("Sum of elements in the list is:", sum)
print("Multiplication of elements in the list is:", mul)
