import random, os, string

def drawHangman(hangman_art, num):
    print("***********************", end="")
    print("\n\t___\n\t   |")
    for i in hangman_art[num]:
        print("\t " + i)
    print()
    print("***********************")
    
def printWords(word, foundLetters):
    completed = True
    for i in word:
        if i.lower() in foundLetters:
            print(i, end=" ")
        elif i == " ":
            print(" ", end=" ")
        elif i in string.punctuation:
            print(i, end="")
        else:
            print("_", end=" ")
            completed = False
    print("\t")
    return completed

def main():
    words = ("Inception", "The Shawshank Redemption", "The Godfather", "Pulp Fiction", "Forrest Gump", "The Dark Knight", "Schindler's List", "Fight Club", "The Matrix", "The Silence of the Lambs", "Jurassic Park", "Star Wars: A New Hope", "The Lord of the Rings: The Fellowship of the Ring", "Back to the Future", "Gladiator", "Titanic", "Saving Private Ryan", "The Terminator", "Goodfellas", "The Lion King", "Braveheart", "Raiders of the Lost Ark", "The Green Mile", "Se7en", "The Usual Suspects", "The Sixth Sense", "Alien", "Jaws", "Toy Story", "The Prestige", "A Clockwork Orange", "Casablanca", "Blade Runner", "E.T. the Extra-Terrestrial", "The Departed", "Die Hard", "Indiana Jones and the Last Crusade", "The Big Lebowski", "American Beauty", "Memento", "12 Angry Men", "Raging Bull", "Citizen Kane", "Gone with the Wind", "The Grand Budapest Hotel", "Mad Max: Fury Road", "The Revenant", "The Wolf of Wall Street", "No Country for Old Men", "There Will Be Blood", "The Social Network", "Inglourious Basterds", "La La Land", "Whiplash", "Get Out", "The Avengers", "Guardians of the Galaxy", "Her", "Interstellar", "Django Unchained", "The Hurt Locker", "The Imitation Game", "Moonlight", "Black Swan", "Gravity", "Slumdog Millionaire", "A Beautiful Mind", "The King's Speech", "The Pianist", "The Girl with the Dragon Tattoo", "Birdman", "12 Years a Slave", "Shutter Island", "The Revenant", "Zero Dark Thirty", "Argo", "Mad Max: Fury Road", "The Shape of Water", "The Grand Budapest Hotel", "Silver Linings Playbook", "Drive", "Ex Machina", "Looper", "Spotlight", "Prisoners", "The Conjuring", "The Dark Knight Rises", "Inception", "The Departed", "No Country for Old Men", "The Curious Case of Benjamin Button", "Pan's Labyrinth", "Eternal Sunshine of the Spotless Mind", "Sin City", "The Bourne Identity", "Minority Report", "Catch Me If You Can", "The Incredibles", "Finding Nemo", "Monsters, Inc.", "Inside Out")

    hangman_art = {
        0: ("    ", "    ", "    "),
        1: ("  O ", "    ", "    "),
        2: ("  O ", "  | ", "    "),
        3: ("  O ", "  | ", " /  "),
        4: ("  O ", "  | ", " / \\"),
        5: ("  O ", " /| ", " / \\"),
        6: ("  O ", " /|\\", " / \\"),}
    
    while True:
        foundLetters = []
        usedLetters = []
        word = str(words[random.randint(0, len(words))])
        counter = 0
        choice = input("\nPlay? (Y/N)\n")
        if choice.lower() == "y":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice.lower() == "n":
            break
        else:
            print("Invalid answer")
            continue

        while True:
            drawHangman(hangman_art, counter)
            print("\n")
            found = printWords(word, foundLetters)
            if found:
                break
            if counter >= 6:
                print("\nAnswer : " + word)
                break
            print("\n\n")
            guess = input("Enter Your Guess : ")
            
            if not guess.isalnum():
                break
            if len(guess) != 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"'{guess}' invalid guess.")
                continue
            if guess in usedLetters:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"'{guess}' is used before.")
                continue

            usedLetters.append(guess.lower())

            if word.lower().find(guess.lower()) == -1:
                counter += 1
            else:
                for i in range(0, word.lower().count(guess.lower())):
                    foundLetters.append(guess.lower())
            os.system('cls' if os.name == 'nt' else 'clear')
    
if __name__ == "__main__":
    main()