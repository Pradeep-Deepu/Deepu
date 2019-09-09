def find_longest_word():
    x=[]

    n=int(input("enter size of list:"))
    for i in range(0,n):
        elements=str(input())
        x.append(elements)
    print(max(x))
find_longest_word()    
