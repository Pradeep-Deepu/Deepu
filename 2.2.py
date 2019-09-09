def max_in_list():
    x=[]
    m=int(input("enter the size:"))
    for i in range(0,m):
        elements=int(input())
        x.append(elements)
    large=0
    for num in x:
        if num > large:
            large=num
    print("The largest number in the list is:",large)
max_in_list()    
        
