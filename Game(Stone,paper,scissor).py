try:   
    import random,time
    def game():
        print("Choose What Do You Wnat(stone , paper, scissor)")
        user = input("ENTER HERE:\n")
        lst = ["stone","paper","scissor"]
        CPU = random.choice(lst)
        if user == "stone" and CPU == "stone":
            print("CPU Chose stone\n")
            print("Game Tied")
            
        elif user == "stone" and CPU == "paper":
            print("CPU Chose paper\n")
            print("You lose !")
        elif user == "stone" and CPU == "scissor":
            print("CPU Chose scissor\n")
            print("You Won !")
            
        if user == "paper" and CPU == "stone":
            print("CPU Chose stone\n")
            print("You Won !")
        elif user == "paper" and CPU == "paper":
            print("CPU Chose paper\n")
            print("Game Tied !")
        elif user == "paper" and CPU == "scissor":
            print("CPU Chose scissor\n")
            print("You Lose !")

        if user == "scissor" and CPU == "stone":
            print("CPU Chose stone\n")
            print("You Lose !")
        elif user == "scissor" and CPU == "paper":
            print("CPU Chose paper\n")
            print("You Won !")
        elif user == "scissor" and CPU == "scissor":
            print("CPU Chose scissor\n")
            print("Game Tied !")

    game()
    localtime =time.time()
    print(localtime)
    game()
    localtime =time.time()
    print(localtime)
    game()
    localtime =time.time()
    print(localtime)
    game()
    localtime =time.time()
    print(localtime)
    game()
    localtime =time.time()
    print(localtime)
    game()
    localtime =time.time()
    print(localtime)

        
    print(" Enjoy Your Game")

except Exception as A:
    print(A)

