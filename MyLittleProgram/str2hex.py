import binascii #Import the lib..
a = "1" 
while a == "1":
    textin = str(input("Please input some words(Enter $^_^stop to stop the loop.):"))     #Input the words.
    if textin.lower() == "$^_^stop":    #Check if the user want to stop the loop.('.lower()' means let A turn to a).
        break   #Stop the loop.
    utf8out = binascii.b2a_hex(textin.encode("utf8"))   #Encode the words which have been inputed.
    print (utf8out)     #Print the hex of the words.
    print ("Recheck the hex text:" + str(binascii.a2b_hex(utf8out).decode("utf8")))     #Recheck the hex(decode the hex to string) and print out.
print ("The loop is end.")
