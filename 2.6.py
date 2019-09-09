c=str(input("Enter your string"))
c=c.replace(" ","")
print(c)
c1=c[::-1]
print(c1)
if c==c1:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
    
