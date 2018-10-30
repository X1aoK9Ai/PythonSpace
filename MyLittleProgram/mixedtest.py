num = 23
runningbig = True

while runningbig:

    running = True

    while running:
        guess = str(input("Please enter a number:"))
        isdigit = str.isdigit(guess)
        if isdigit == True:
            print("It\'s a digit.")
            running = False
        elif isdigit == False:
            print("Please input a digit.")

    guess = int(guess)

    if guess == num:
        print("Congratulations!")
        runningbig = False
    elif guess < num:
        print("It\'s a little small. Try a bigger one!")
    elif guess > num:
        print("It\'s a little big. Try a smaller one!")

else:
    print("The loop is over.")

print("Done.")
