print ('Welcome!')
def oneortwo(a,b):      #Delimit a function.
    a=int(a)            #Delimit function params.
    b=int(b)            #
    if a>b:             #if loop in the function.
        print (a,"is the bigger one.")
    else:
        print (b,"is the bigger one.")
a=input(("a = "))       #Input the a.
b=input(("b = "))       #Input the b.
oneortwo(a,b)           #Transfer the function which we have delimited.
