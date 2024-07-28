import random as r
ran = int(r.randrange(1, 100))
print("Enter Your Name : ")
name = input()
print("Welcome", name, "In Guess The Right Number Game.")
print("Enter the number of attempts")
attempts = int(input())
i = 0
while i < attempts:
    print("\n\t<------ATTEMPT No :", i+1, "------>")
    print("Choose the number between 1 to 100: ")
    user = int(input())
    if user == ran:
        print("Congratulations You Guess the Right Number.")
        break
    elif user >= ran:
        print("Entered Number was Too High.")
    elif user <= ran:
        print("Entered Number was Too Low ")
    else:
        print("Try Again!! Your  entered numbers should be From 0 to 100")
    i = i+1
    if attempts == i :
        print("OOPS !! You Lose :( \nThe Correct Number was", ran)