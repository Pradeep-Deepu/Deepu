
a=[]
n= int(input("size of list 'a':"))
for i in range(0,n):
    elements= input()
    a.append(elements)
print("Your list is:",a)
x= (input("Enter your value:"))
for num in a:
    if x==num:
        print("true")
        break
if x != num:
    print("false")
       
    
