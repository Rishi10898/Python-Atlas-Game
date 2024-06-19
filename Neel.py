def getLives():
    while True:
        lives = input("How many lives do you want to do this game?")
        try:
            lives - int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please pick a number for this question.")
        except:
            print("Please input a number(The reason you are seeing this message is because you didn't input a number for this question the first time around).")