import binascii #Import the lib..
a = 1
people = str(binascii.a2b_hex('e69d8ee6809de99ba8').decode("utf8"))

while a == 1:
    print("我喜欢" + people)

    while a == 1:
        yesornot = input("Once again? (y/n):")

        yesornot = str.lower(yesornot)
        
        if yesornot == 'yes' or yesornot == 'y':
            break
        elif yesornot == 'no' or yesornot == 'n':
            a = 0
        else:
            print("Please input 'Yes' or 'Y' or 'No' or 'N'")

else:
    print("我永远喜欢" + people + ".")
