def filter_long_words():
    x=[]
    y=[]
    n=int(input("Enter the size of the list:"))
    for i in range(0,n):
        elements=str(input())
        x.append(elements)
    num=int(input("Enter threshold:"))
    if len(elements)>num:
        y.append(elements)
    print(y)
filter_long_words()
