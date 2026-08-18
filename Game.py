import random

Secret = random.randint(1,12)

attempt = 0

while True:
    guess = int(input("Enter the number : "))

    attempt+=1

    if guess == Secret:
        print(f"You guessed the number in {attempt} attempt.")
        break
    elif guess < Secret:
        print("Too low")
    elif guess > Secret:
        print ("Too high")

    if attempt > 5:
        print("You lose because attempts are over")
   
        
    
