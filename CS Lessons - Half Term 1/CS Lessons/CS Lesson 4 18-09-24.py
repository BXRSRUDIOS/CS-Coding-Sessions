from random import randint

def computer_guess(num):
    low = 1
    high = 1000
    count = 0
    guess = (low+high)//2
    while guess != num:
        count +=1
        print("The computer guessed", guess, "and it's wrong. This is attempt", count)
        if guess > num:
            high = guess
        elif guess < num:
            low = guess + 1
        guess = (low+high)//2   

    print("The computer guessed", guess, "and it was correct! Completed after", count+1, "attempts")


def main():
    num = int(input("Enter a number: "))
    if num < 1 or num > 1000:
        print("Must be in range [1, 1000]")
    else:
        computer_guess(num)

if __name__ == '__main__':
    main()