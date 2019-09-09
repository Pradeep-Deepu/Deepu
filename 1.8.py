x=[]
y=[]
n1=int(input("Enter the size of list_1:"))
for i in range(0,n1):
    elements=input()
    x.append(elements)
print("Your list_1 is:",x)
n2=int(input("Enter the size of list_2:"))
for j in range(0,n2):
    ele=input()
    y.append(ele)
print("Your list_2 is:",y)
for num1 in x:
    for num2 in y:
        if num1==num2:
            print("true")
            break
if num1!=num2:
    print("false")
            
