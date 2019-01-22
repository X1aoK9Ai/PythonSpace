#!usr/bin/python3
# Filename: return_try.py
def aAndb(x,y):
    if x>y:
        a = int(x)-int(y)
        return a
    else:
        a = int(y)-int(x)
        return a
x = input("Please input 'x':")
y = input("Please input 'y':"")
print(aAndb(x,y))
print("------------------------------------")
print("I'm going to print x and y.")
print(x + y)
print("---------")
print("x=" + x)
print("y=" + y)
print("End.")
