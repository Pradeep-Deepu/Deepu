import string
alphabet = set(string.ascii_lowercase)
c=str(input("Enter your string"))
print(alphabet)
print(set(c.lower()))
print(set(c.lower()) >= alphabet)
