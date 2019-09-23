from random import randrange

to_guess = randrange(100)
print("Guess the number!")

run = True
while run:
    guess = input("Guess?")
    if guess.isdigit():
        n = int(guess)
        if n < to_guess:
            print("plus")
        elif n > to_guess:
            print("moins")
        else:
            print("Félicitations! vous avez trouvé le nombre: " + str(n) + "!")
            run = False
    else:
        print("Ceci n'est pas un nombre valide, réessayez.")
