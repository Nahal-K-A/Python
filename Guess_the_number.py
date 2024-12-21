import random

stop = 0
while stop == 0:
    flag = 0
    count = 0
    start = input("I have a number in my mind, Will you guess it? (y/n)").lower()
    num = random.randint(1, 100)
    while flag == 0:
        try:
            if start == "y":
                guess = int(input("Guess the number b/w 1 & 100: "))
                count += 1
                while True:
                    if guess < num:
                        guess = int(input("Guess higher"))
                        count += 1
                    elif guess > num:
                        guess = int(input("Guess lower"))
                        count += 1
                    else:
                        print("You guessed the correct num :", num)
                        print(f"no. of guess: {count}")
                        flag = 1
                        break
            elif start == "n":
                print("Thank you for playing")
                stop = 1
                break
            else:
                print("Invalid Choice!")
        except ValueError:
            print("Enter a valid number")
