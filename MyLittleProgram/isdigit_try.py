running = True
while running:
    guess = str(input("Please enter a number:"))
    isdigit = str.isdigit(guess)
    if isdigit == True:
        print("True")
    else:
        print("False")
else:
    print("Done.")
